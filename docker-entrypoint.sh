#!/bin/bash
echo "Sleeping for 3 seconds"
sleep 3;
echo "Starting FastAPI Server"
fastapi run app/main.py --port 80
