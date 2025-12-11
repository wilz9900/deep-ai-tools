#!/data/data/com.termux/files/usr/bin/bash
# DDoS Toolkit Installer for Termux
# Auto-install semua dependencies

echo "[+] Installing DDoS Toolkit..."

# Update system
pkg update -y && pkg upgrade -y

# Install Python
pkg install python -y
pkg install python3 -y
pip install --upgrade pip

# Install dependencies
pip install requests colorama tqdm bs4 cfscrape cloudscraper

# Install tools
pkg install git wget curl nmap netcat openssl tor proxychains-ng -y

# Create directory
mkdir -p ~/ddos-toolkit
cd ~/ddos-toolkit

# Download scripts
wget https://raw.githubusercontent.com/deep-ai-tools/termux-ddos/main/ddos.py
wget https://raw.githubusercontent.com/deep-ai-tools/termux-ddos/main/ddos_gui.py
wget https://raw.githubusercontent.com/deep-ai-tools/termux-ddos/main/layer4_attack.py
wget https://raw.githubusercontent.com/deep-ai-tools/termux-ddos/main/config.json

# Make executable
chmod +x ddos.py ddos_gui.py layer4_attack.py

echo "[+] Installation complete!"
echo "[+] Run: python ddos.py"
