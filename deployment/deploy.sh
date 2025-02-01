#!/bin/bash

# Deployment script for the phishing detection system

echo "Starting deployment..."

# Step 1: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 2: Run database migrations (if any)
echo "Running migrations..."
python src/utils/migrate.py

# Step 3: Start the API server
echo "Starting API server..."
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 &

echo "Deployment completed successfully!"