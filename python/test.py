import keyboard

class kkk:
    def __init__(self):
        self.keys = []

    def do(self, event: keyboard.KeyboardEvent):
        key = event.name

        if event.event_type == "down":
            if key and key not in self.keys:
                self.keys.append(key)

        elif event.event_type == "up":
            if key in self.keys:
                self.keys.remove(key)

        # فلترة المفاتيح الفاضية قبل استخدامها
        clean_keys = [k for k in self.keys if k]
        try:
            combo = keyboard.get_hotkey_name(clean_keys)
            keys_split = combo.split('+') if combo else []
            print(keys_split)
        except ValueError as e:
            print("⚠️ حدث خطأ:", e)

    def did(self):
        keyboard.hook(self.do)
        keyboard.wait("esc")
        print("Final keys:", self.keys)

k = kkk()
k.did()
