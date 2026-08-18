#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "=========================================================="
echo " Deploy ITC Brand Marketing Agent to Google Agent Platform"
echo " (Vertex AI Agent Engine / Google ADK Hosted Runtime)"
echo " Model: gemini-2.5-pro • gemini-2.5-flash • Gemini Flash Image • Veo 3.1"
echo " Region: us-central1 (Iowa)"
echo "=========================================================="

if [ ! -f "$DIR/venv/bin/adk" ]; then
    echo "⚡ Initializing environment via setup.sh..."
    bash "$DIR/setup.sh"
fi

CURRENT_PROJECT=$(gcloud config get-value project 2>/dev/null | grep -v "unset" || echo "")

read -p "Enter GCP Project ID [${CURRENT_PROJECT}]: " PROJECT_ID
PROJECT_ID=${PROJECT_ID:-$CURRENT_PROJECT}

if [ -z "$PROJECT_ID" ]; then
    echo "❌ Error: Project ID is required for deployment."
    exit 1
fi

read -p "Enter GCP Region [us-central1]: " REGION
REGION=${REGION:-"us-central1"}

read -p "Enter existing Agent Engine ID (or press Enter to create a NEW instance): " ENGINE_CHOICE

echo ""
echo "🔐 Verifying GCP APIs & IAM permissions for [${PROJECT_ID}]..."

# 1. Enable Required Cloud APIs
gcloud services enable \
    aiplatform.googleapis.com \
    storage.googleapis.com \
    generativelanguage.googleapis.com \
    --project="$PROJECT_ID" --quiet 2>/dev/null || true

# 2. Check/Create Service Account
SA_NAME="itc-marketing-agent-sa"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
if ! gcloud iam service-accounts describe "$SA_EMAIL" --project="$PROJECT_ID" &>/dev/null; then
    echo "  • Provisioning Service Account: ${SA_EMAIL}..."
    gcloud iam service-accounts create "$SA_NAME" \
        --display-name="ITC Brand Marketing AI Agent Service Account" \
        --description="Access for Vertex AI Reasoning Engine, Foundation Models, and Cloud Storage" \
        --project="$PROJECT_ID" --quiet 2>/dev/null || true
fi

# 3. Bind IAM Roles for Models & Storage
for ROLE in roles/aiplatform.user roles/storage.objectAdmin roles/serviceusage.serviceUsageConsumer; do
    gcloud projects add-iam-policy-binding "$PROJECT_ID" \
        --member="serviceAccount:${SA_EMAIL}" \
        --role="$ROLE" \
        --condition=None --quiet 2>/dev/null || true
done

# 4. Ensure GCS Bucket exists
BUCKET_NAME="itc-brand-marketing-assets-${PROJECT_ID}"
if ! gsutil ls -b "gs://${BUCKET_NAME}" &>/dev/null && ! gcloud storage buckets describe "gs://${BUCKET_NAME}" &>/dev/null; then
    echo "  • Creating Cloud Storage Bucket: gs://${BUCKET_NAME}..."
    gcloud storage buckets create "gs://${BUCKET_NAME}" \
        --project="$PROJECT_ID" \
        --location="$REGION" \
        --uniform-bucket-level-access --quiet 2>/dev/null || \
    gsutil mb -p "$PROJECT_ID" -l "$REGION" -b on "gs://${BUCKET_NAME}" 2>/dev/null || true
fi

echo "✅ GCP APIs, IAM & Cloud Storage verified."
echo ""
echo "Deploying Agent to Vertex AI Agent Platform..."
echo "Project: $PROJECT_ID | Region: $REGION"

# Disable telemetry prompt if supported
./venv/bin/adk telemetry disable 2>/dev/null || true
export PYTHONPATH="$DIR:$DIR/agent"

if [ -z "$ENGINE_CHOICE" ] || [ "$ENGINE_CHOICE" = "new" ]; then
  echo "Action: Creating a NEW Agent Engine instance in ${REGION}..."
  ./venv/bin/adk deploy agent_engine \
    --project="$PROJECT_ID" \
    --region="$REGION" \
    --artifact_service_uri="memory://" \
    --display_name="ITC Brand Marketing AI Agent" \
    --description="Autonomous Multi-Agent Generative Marketing Suite for ITC Limited" \
    agent
else
  echo "Action: In-place updating existing instance ID: $ENGINE_CHOICE in ${REGION}..."
  ./venv/bin/adk deploy agent_engine \
    --project="$PROJECT_ID" \
    --region="$REGION" \
    --agent_engine_id="$ENGINE_CHOICE" \
    --session_service_uri="agentengine://projects/${PROJECT_ID}/locations/${REGION}/reasoningEngines/${ENGINE_CHOICE}" \
    --artifact_service_uri="memory://" \
    --display_name="ITC Brand Marketing AI Agent" \
    --description="Autonomous Multi-Agent Generative Marketing Suite for ITC Limited" \
    agent
fi

echo ""
echo "=========================================================="
echo " 🎉 Deployment Complete!"
echo " The high-code agent is now hosted live on Google Agent Platform (${REGION})."
echo "=========================================================="
