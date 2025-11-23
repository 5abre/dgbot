#!/bin/bash

export PYTHONPATH="$PWD/src:$PYTHONPATH"
echo "Get started..."

if [ "$1" == "bot" ]; then
    echo "Starting bot"
    poetry run python src/dgbot/bot/main.py
elif [ "$1" == "web" ]; then
    echo "Starting application"
    poetry run python src/dgbot/web/app.py
else
    echo "bot - запустить бота"
    echo "web - запустить веб-сервер"
fi