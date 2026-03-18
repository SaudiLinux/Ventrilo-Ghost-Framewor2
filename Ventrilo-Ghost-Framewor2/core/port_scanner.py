import socket
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self, target):
        self.target = target.split("//")[-1].split("/")[0]
        self.common_ports = [21, 22, 80, 443, 3306, 8080]

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((self.target, port)) == 0:
                    print(f"[🔥 PORT FOUND] {port} is OPEN (Service Detected)")
                    return port
        except: return None

    def run(self):
        print(f"[*] بدء فحص المنافذ للسيرفر: {self.target}")
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.scan_port, self.common_ports)