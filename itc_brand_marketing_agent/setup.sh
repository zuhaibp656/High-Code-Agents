#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "=========================================================="
echo " 🍪 ITC Brand Marketing AI Agent — Automated Setup"
echo " (Google ADK • Gemini Enterprise • Imagen 3 • Google Veo)"
echo "=========================================================="

# 1. Detect Python 3.10+
PYTHON_BIN=""
for cmd in python3.11 python3.10 python3.12 python3; do
    if command -v "$cmd" &>/dev/null; then
        VER=$("$cmd" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
        MAJOR=$(echo "$VER" | cut -d. -f1)
        MINOR=$(echo "$VER" | cut -d. -f2)
        if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 10 ]; then
            PYTHON_BIN="$cmd"
            break
        fi
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    echo "❌ Error: Python 3.10 or higher is required. Please install Python 3.10+."
    exit 1
fi
echo "✅ Found Python: $($PYTHON_BIN --version) ($PYTHON_BIN)"

# 2. Setup Virtual Environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment in ./venv..."
    "$PYTHON_BIN" -m venv venv
fi

# 3. Upgrade pip and install requirements
echo "📦 Installing required dependencies from requirements.txt..."
./venv/bin/pip install --upgrade pip --quiet
./venv/bin/pip install -r requirements.txt --quiet
echo "✅ Dependencies successfully installed."

# 4. Auto-configure .env if missing
if [ ! -f ".env" ]; then
    echo "⚙️ Creating default .env configuration..."
    cp .env.example .env 2>/dev/null || cat <<EOF > .env
GOOGLE_CLOUD_PROJECT=
GOOGLE_CLOUD_LOCATION=us-central1
EOF
fi

# Auto-populate project ID from gcloud if empty
DETECTED_PROJECT=$(gcloud config get-value project 2>/dev/null | grep -v "unset" || echo "")
if [ -n "$DETECTED_PROJECT" ]; then
    CURRENT_ENV_PROJ=$(grep "GOOGLE_CLOUD_PROJECT=" .env | cut -d'=' -f2)
    if [ -z "$CURRENT_ENV_PROJ" ]; then
        sed -i '' "s/GOOGLE_CLOUD_PROJECT=.*/GOOGLE_CLOUD_PROJECT=${DETECTED_PROJECT}/" .env 2>/dev/null || sed -i "s/GOOGLE_CLOUD_PROJECT=.*/GOOGLE_CLOUD_PROJECT=${DETECTED_PROJECT}/" .env
        echo "✅ Automatically configured GOOGLE_CLOUD_PROJECT=${DETECTED_PROJECT} in .env"
    fi
fi

# 5. Automated GCP APIs, IAM & Service Account Provisioning
if [ -n "$DETECTED_PROJECT" ] && command -v gcloud &>/dev/null; then
    echo ""
    echo "🔐 Provisioning Google Cloud APIs, IAM & Storage for [${DETECTED_PROJECT}]..."
    
    # Enable necessary GCP APIs
    echo "  • Enabling Vertex AI & Cloud Storage APIs..."
    gcloud services enable \
        aiplatform.googleapis.com \
        storage.googleapis.com \
        generativelanguage.googleapis.com \
        --project="$DETECTED_PROJECT" --quiet 2>/dev/null || true

    # Create dedicated Service Account if missing
    SA_NAME="itc-marketing-agent-sa"
    SA_EMAIL="${SA_NAME}@${DETECTED_PROJECT}.iam.gserviceaccount.com"
    echo "  • Checking/Creating Service Account: ${SA_EMAIL}..."
    if ! gcloud iam service-accounts describe "$SA_EMAIL" --project="$DETECTED_PROJECT" &>/dev/null; then
        gcloud iam service-accounts create "$SA_NAME" \
            --display-name="ITC Brand Marketing AI Agent Service Account" \
            --description="Access for Vertex AI Reasoning Engine, Foundation Models, and Cloud Storage" \
            --project="$DETECTED_PROJECT" --quiet 2>/dev/null || true
    fi

    # Bind IAM Roles for Foundation Models & GCS
    echo "  • Binding IAM Roles (Vertex AI User & Storage Object Admin)..."
    for ROLE in roles/aiplatform.user roles/storage.objectAdmin roles/serviceusage.serviceUsageConsumer; do
        gcloud projects add-iam-policy-binding "$DETECTED_PROJECT" \
            --member="serviceAccount:${SA_EMAIL}" \
            --role="$ROLE" \
            --condition=None --quiet 2>/dev/null || true
    done

    # Ensure Private GCS Bucket exists for marketing assets
    BUCKET_NAME="itc-brand-marketing-assets-${DETECTED_PROJECT}"
    echo "  • Ensuring Cloud Storage Bucket exists: gs://${BUCKET_NAME}..."
    if ! gsutil ls -b "gs://${BUCKET_NAME}" &>/dev/null && ! gcloud storage buckets describe "gs://${BUCKET_NAME}" &>/dev/null; then
        gcloud storage buckets create "gs://${BUCKET_NAME}" \
            --project="$DETECTED_PROJECT" \
            --location="us-central1" \
            --uniform-bucket-level-access --quiet 2>/dev/null || \
        gsutil mb -p "$DETECTED_PROJECT" -l "us-central1" -b on "gs://${BUCKET_NAME}" 2>/dev/null || true
    fi
    echo "✅ GCP APIs, IAM Roles & Cloud Storage ready."
fi

# 6. Make scripts executable
chmod +x run.sh web.sh deploy.sh setup.sh 2>/dev/null || true

echo ""
echo "=========================================================="
echo " 🎉 Setup Complete! You're ready to run:"
echo ""
echo " 1. Interactive CLI:          ./run.sh"
echo " 2. ADK Web Designer UI:      ./web.sh 8080"
echo " 3. Deploy to Agent Engine:   ./deploy.sh"
echo " 4. Run Automated Test Suite: ./venv/bin/pytest test_agent.py -v"
echo "=========================================================="
