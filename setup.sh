#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if the script is being run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "[+] Please run this script with sudo or as root."
    exit 1
fi

# Update package manager repositories
echo "[+] Updating package repositories..."
apt-get update -y

# Install required system packages
echo "[+] Installing system packages..."
apt-get install -y python3 ffmpeg imagemagick

# Check if Python 3 is installed
if ! command_exists python3; then
    echo "[-] Python 3 is not installed. Please install Python 3 manually and run this script again."
    exit 1
fi

# Install Python dependencies using pip
echo "[+] Installing Python dependencies..."
pip3 install -r src/requirements.txt

echo "[+] Setup completed successfully!"
