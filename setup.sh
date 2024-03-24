#!/bin/bash

# Check if the user is root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r src/requirements.txt

# Install Linux tools (ffmpeg and imagemagick)
echo "Installing Linux tools..."
apt-get update
apt-get install -y ffmpeg imagemagick

echo "Setup complete."
