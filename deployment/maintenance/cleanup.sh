#!/bin/bash
# Script to clean up old logs and temporary files

LOG_DIR="../logs"
TEMP_DIR="/tmp/phishing-detection"

echo "Cleaning up logs and temporary files..."

# Delete logs older than 7 days
find $LOG_DIR -type f -name "*.log" -mtime +7 -exec rm -f {} \;

# Clean up temporary files
rm -rf $TEMP_DIR/*

echo "Cleanup completed."