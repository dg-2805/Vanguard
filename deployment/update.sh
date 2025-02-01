#!/bin/bash

# Update script for the phishing detection system

echo "Starting update..."

# Step 1: Pull the latest code
echo "Pulling latest code..."
git pull origin main

# Step 2: Restart the API server
echo "Restarting API server..."
pkill -f "uvicorn src.api.main:app"
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 &

echo "Update completed successfully!"