#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

if [ ! -f "venv/bin/python" ]; then
    echo "⚡ Initializing environment via setup.sh..."
    bash "$DIR/setup.sh"
fi

PYTHON_CMD="./venv/bin/python"
export PYTHONPATH="$DIR:$DIR/agent"
$PYTHON_CMD main.py
