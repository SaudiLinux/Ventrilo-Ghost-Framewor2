import os
import sys
import subprocess

# بيانات المشروع والمطور (SayerLinux)
PROJECT_NAME = "Ventrilo-Ghost-Framework"
DEVELOPER = "SayerLinux"
VERSION = "2.5.0-GodMode"

def run_command(command):
    """تنفيذ أوامر النظام وعرض النتائج بشكل احترافي"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + command.split())
        return True
    except Exception as e:
        print(f"[\033[91m!\033[0m] خطأ في التثبيت: {e}")
        return False

def setup_environment():
    os.system('clear')
    print(f"\033[94m" + "#"*60)
    print(f"#  {PROJECT_NAME} // {DEVELOPER} // {VERSION}  #")
    print("#"*60 + "\033[0m")
    
    print("\n[*] جاري تهيئة بيئة العمل في Kali Linux...")

    # 1. قائمة المكتبات الضرورية (Requirements)
    dependencies = "requests aiohttp beautifulsoup4 flask colorama cryptography"
    print(f"[*] جاري تثبيت المكتبات: {dependencies}...")
    if run_command(dependencies):
        print("[\033[92m✔\033[0m] تم تثبيت كافة المكتبات بنجاح.")
    
    # 2. إنشاء هيكلية المجلدات إذا كانت مفقودة
    folders = ['core', 'c2_server', 'c2_server/templates', 'agent']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[\033[92m+\033[0m] تم إنشاء المجلد: {folder}")

    # 3. التأكد من وجود ملفات التنشيط (__init__.py)
    init_files = ['core/__init__.py', 'c2_server/__init__.py', 'agent/__init__.py']
    for init_file in init_files:
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write(f"# Initialized by SayerLinux Setup\nVERSION = '{VERSION}'\n")
            print(f"[\033[92m✔\033[0m] تم تهيئة الملف: {init_file}")

    # 4. إنشاء ملف التقرير الافتراضي
    if not os.path.exists("vulnerability_report.txt"):
        with open("vulnerability_report.txt", "w") as f:
            f.write(f"--- Ventrilo-Ghost Vulnerability Report ---\nCreated by: {DEVELOPER}\n")

    print(f"\n\033[92m{'='*60}\n[🌟] مبروك يا {DEVELOPER}! الأداة جاهزة الآن للعمل بنسبة 100%.\n{'='*60}\033[0m")
    print(f"\n[!] لتشغيل الأداة الآن، اكتب: \033[93mpython3 main.py\033[0m\n")

if __name__ == "__main__":
    setup_environment()