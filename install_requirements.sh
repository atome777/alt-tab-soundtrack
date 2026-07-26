#!/bin/bash

if [ ! -d "venv" ]; then
    python3 -m venv venv

    source venv/bin/activate
    pip install --upgrade pip
    python3 -m pip install python-dotenv aiomysql typing_extensions aiohttp aiofiles asyncpg aio-pika redis pydantic aiocache
fi

playwright install chromium
playwright install msedge

pip list