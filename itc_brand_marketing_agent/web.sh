#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PORT=${1:-8080}

if [ ! -f "$DIR/venv/bin/adk" ]; then
    echo "⚡ Initializing environment via setup.sh..."
    bash "$DIR/setup.sh"
fi

if [ -f "$DIR/.env" ]; then
    set -a
    source "$DIR/.env"
    set +a
fi

echo "=========================================================="
echo " Starting Google ADK Web UI / Agent Designer"
echo " Target Port: http://127.0.0.1:${PORT}"
echo "=========================================================="

export PYTHONPATH="$DIR:$DIR/agent"
./venv/bin/adk web --port="$PORT" agent
