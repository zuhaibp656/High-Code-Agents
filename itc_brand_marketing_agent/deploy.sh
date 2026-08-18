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

CURRENT_PROJECT=$(gcloud config get-value project 2>/dev/null | grep -v "unset" || echo "")

read -p "Enter GCP Project ID [${CURRENT_PROJECT}]: " PROJECT_ID
PROJECT_ID=${PROJECT_ID:-$CURRENT_PROJECT}

read -p "Enter GCP Region [us-central1]: " REGION
REGION=${REGION:-"us-central1"}

read -p "Enter existing Agent Engine ID (or press Enter to create a NEW instance): " ENGINE_CHOICE

echo ""
echo "Deploying Agent to Vertex AI Agent Platform..."
echo "Project: $PROJECT_ID | Region: $REGION (us-central1)"

# Disable telemetry prompt if supported
./venv/bin/adk telemetry disable 2>/dev/null || true
export PYTHONPATH="$DIR:$DIR/agent"

if [ -z "$ENGINE_CHOICE" ] || [ "$ENGINE_CHOICE" = "new" ]; then
  echo "Action: Creating a NEW Agent Engine instance in us-central1..."
  ./venv/bin/adk deploy agent_engine \
    --project="$PROJECT_ID" \
    --region="$REGION" \
    --artifact_service_uri="memory://" \
    --display_name="ITC Brand Marketing AI Agent" \
    --description="Autonomous Multi-Agent Generative Marketing Suite for ITC Limited" \
    agent
else
  echo "Action: In-place updating existing instance ID: $ENGINE_CHOICE in us-central1..."
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
echo " Deployment Complete!"
echo " The high-code agent is now hosted live on Google Agent Platform (us-central1)."
echo "=========================================================="
