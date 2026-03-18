import socket

class GhostOSINT:
    def __init__(self, target):
        self.domain = target.split("//")[-1].split("/")[0]
        # قائمة بأكثر النطاقات الفرعية شيوعاً واستهدافاً
        self.subs = ["admin", "dev", "test", "api", "db", "mail", "cloud", "vpn", "beta"]

    def find_subdomains(self):
        print(f"\n{'-'*20}\n[*] استطلاع النطاقات الفرعية لـ: {self.domain}\n{'-'*20}")
        found = []
        for sub in self.subs:
            url = f"{sub}.{self.domain}"
            try:
                ip = socket.gethostbyname(url)
                print(f"[🔥 SUB FOUND] {url} -> {ip}")
                found.append(url)
            except: pass
        return found