import asyncio
from core.scanner import GhostScanner
from core.exploiter import GhostExploiter
from core.passive_scanner import PassiveScanner

class AutoPwn:
    def __init__(self, target):
        self.target = target
        self.scanner = GhostScanner(target)
        self.exploiter = GhostExploiter(target)
        self.passive = PassiveScanner(target)

    async def execute_chain(self):
        print(f"\n[☢] تفعيل بروتوكول AUTO-PWN الشامل...")
        
        # 1. الاستطلاع الصامت
        self.passive.run_recon()
        
        # 2. الزحف واستخراج كافة الروابط
        await self.scanner.start()
        
        # 3. الهجوم الآلي على كل رابط تم اكتشافه
        print(f"[*] جاري مهاجمة {len(self.scanner.visited)} رابط تم اكتشافهم...")
        for url in self.scanner.visited:
            if "?" in url:
                # استخراج اسم المعامل (Parameter) وتجربة SQLi و LFI فوراً
                try:
                    param = url.split("?")[1].split("=")[0]
                    self.exploiter.verify_sqli(param)
                    self.exploiter.test_lfi(param)
                except: pass
        
        print(f"\n[✔] اكتمل الهجوم الآلي بنجاح. راجع التقرير يا SayerLinux.")