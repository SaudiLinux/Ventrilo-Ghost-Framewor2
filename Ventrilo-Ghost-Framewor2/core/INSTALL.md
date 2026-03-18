# <div align="center"><font color="#007bff">دليل التثبيت والتهيئة // INSTALLATION GUIDE</font></div>

أهلاً بك في نظام **Ventrilo-Ghost v2.5-GodMode**. اتبع هذه الخطوات بعناية لضمان عمل "الترسانة السيبرانية" الخاصة بـ **SayerLinux** بأعلى كفاءة على نظامك.

---

## 📋 المتطلبات المسبقة (Prerequisites)

تأكد من توفر المتطلبات التالية في نظام **Kali Linux** الخاص بك:
- **Python:** إصدار 3.8 أو أحدث.
- **pip3:** مدير حزم بايثون.
- **Git:** لتحميل التحديثات من المستودع.

يمكنك التحقق من المتطلبات عبر الأمر التالي:
```bash
python3 --version && pip3 --version && git --version


⚡ خطوات التثبيت السريع (Quick Installation)

1. تحميل المستودع (Clone)

افتح الـ Terminal وقم بتحميل المشروع من GitHub:


git clone https://github.com/SaudiLinux/Ventrilo-Ghost-Framework.git
cd Ventrilo-Ghost-Framework

2. التشغيل الآلي للمثبت (The Auto-Installer)

لقد قمنا ببرمجة ملف setup.py ليقوم بكافة المهام الصعبة نيابة عنك (تثبيت المكتبات، إنشاء المجلدات، وتهيئة الحزم):


python3 setup.py

سيقوم السكربت بتثبيت requests, aiohttp, flask, cryptography, و colorama تلقائياً.



🚀 كيفية التشغيل (Execution)

تشغيل المحرك الرئيسي (Master Controller)

للوصول لكافة ميزات الفحص، الاستغلال، والتحكم الآلي (Auto-Pwn):


python3 main.py

تشغيل لوحة التحكم المركزية (C2 Dashboard)

إذا كنت تود تشغيل واجهة الويب فقط لإدارة السيرفرات المتصلة:


cd c2_server
python3 app.py

افتح المتصفح على العنوان: http://localhost:5000



🛠️ حل المشاكل الشائعة (Troubleshooting)

1. خطأ "ModuleNotFoundError"

إذا واجهت هذا الخطأ، تأكد من أنك قمت بتشغيل setup.py أولاً، أو قم بتثبيت المكتبات يدوياً:


pip3 install -r requirements.txt

2. صلاحيات التنفيذ (Permissions)

في بعض أنظمة Linux، قد تحتاج لإعطاء صلاحيات للمجلدات:


chmod +x main.py setup.py c2_server/app.py

3. تعارض المنفذ 5000 (Port Conflict)

إذا كانت لوحة التحكم لا تعمل، تأكد من عدم وجود برنامج آخر يستخدم المنفذ 5000:


fuser -k 5000/tcp


📩 الدعم والتواصل (Support)

في حال واجهت أي صعوبة تقنية، يمكنك التواصل مباشرة مع المطور:


Developer: SayerLinux
Email: SaudiLinux1@gmail.com