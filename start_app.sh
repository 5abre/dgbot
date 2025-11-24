#!/bin/bash

export PYTHONPATH="$PWD/src:$PYTHONPATH"
echo "Get started..."

echo "Starting bot"
poetry run python src/dgbot/bot/main.py
