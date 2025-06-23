import xml.etree.ElementTree as ET
import os
import shutil

CONFIG = r"C:\Program Files\VKTablet\config.xml"
BACKUP = r"C:\Program Files\VKTablet\config_backup.xml"

# 1. نسخ نسخة احتياطية أول مرة
if not os.path.exists(BACKUP):
    shutil.copy(CONFIG, BACKUP)

# 2. تحميل الإعداد الرئيسي
tree = ET.parse(CONFIG)
root = tree.getroot()

# مثال: إسم العنصر اللي يحتوي monitor mapping
node = root.find('Mapping/Monitor')
if node is None:
    print("⚠️ لم أجد العنصر المطلوب (Mapping/Monitor)")
    exit(1)

# 3. تغيير القيمة
new_value = "Monitor2" if node.text == "Monitor1" else "Monitor1"
node.text = new_value
tree.write(CONFIG, encoding='utf-8', xml_declaration=True)

print(f"🔁 تم التبديل إلى {new_value}")
