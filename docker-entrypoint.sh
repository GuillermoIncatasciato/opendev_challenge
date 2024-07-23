#!/bin/bash
echo "sleeping for 3 seconds"
sleep 3;
echo "starting server fastapi"
fastapi run app/main.py --port 80
