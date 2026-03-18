import sys, os, asyncio
from colorama import Fore, init

# تهيئة المسارات
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from core.scanner import GhostScanner
from core.exploiter import GhostExploiter
from core.encryptor import GhostEncryptor
from core.passive_scanner import PassiveScanner
from core.autopwn import AutoPwn
from core.osint import GhostOSINT

init(autoreset=True)

def banner():
    print(Fore.CYAN + " #"*35)
    print(Fore.CYAN + f" #  {Fore.WHITE}VENTRILO-GHOST GOD-MODE v2.5 // {Fore.RED}SayerLinux {Fore.CYAN}  #")
    print(Fore.CYAN + " #"*35)

async def main():
    # os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    menu = f"""
    {Fore.RED}[☢] {Fore.WHITE}AUTO-PWN (الهجوم الآلي)    {Fore.YELLOW}[5] {Fore.WHITE}C2 Dashboard (لوحة التحكم)
    {Fore.YELLOW}[1] {Fore.WHITE}Deep Spider (الزحف)        {Fore.YELLOW}[6] {Fore.WHITE}Ghost Encryptor (تشفير)
    {Fore.YELLOW}[2] {Fore.WHITE}OSINT (نطاقات فرعية)       {Fore.YELLOW}[7] {Fore.WHITE}Passive Recon (استطلاع)
    {Fore.YELLOW}[3] {Fore.WHITE}SQLi/LFI Attack (هجوم)     {Fore.YELLOW}[8] {Fore.WHITE}Exit (خروج)
    """
    print(menu)
    choice = input(Fore.RED + "[SayerLinux-Master]> " + Fore.WHITE)

    if choice == '☢' or choice == '9':
        target = input("[?] Target URL: ")
        await AutoPwn(target).execute_chain()
    elif choice == '1':
        target = input("[?] Target URL: ")
        await GhostScanner(target).start()
    elif choice == '2':
        GhostOSINT(input("[?] Target URL: ")).find_subdomains()
    elif choice == '5':
        print(f"{Fore.GREEN}[*] اللوحة تعمل حالياً على http://localhost:5000")
        os.system(f"python3 {os.path.join(BASE_DIR, 'c2_server', 'app.py')}")
    elif choice == '8' or choice == '0':
        sys.exit()

if __name__ == "__main__":
    asyncio.run(main())