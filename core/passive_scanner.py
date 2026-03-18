import requests

class PassiveScanner:
    def __init__(self, target): self.target = target

    def run_recon(self):
        print(f"[*] Recon for: {self.target}")
        try:
            h = requests.get(self.target, timeout=10).headers
            print(f"[+] Server: {h.get('Server', 'Hidden')}")
            print(f"[+] Powered-By: {h.get('X-Powered-By', 'Hidden')}")
            if "X-Frame-Options" not in h: print("[⚠️] Clickjacking Possible (X-Frame Missing)")
        except: pass