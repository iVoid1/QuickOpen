import keyboard
import pynput.keyboard as pKeyboard
import quickopen.module.config as config
import subprocess
quick = 2


configure = config.Config(r"C:\Users\Void\Google_Drive\QuickOpen\python\quickopen\module\actions.json")
keys = []
def search_action(key: keyboard.KeyboardEvent) -> None:
    """Handles key events."""
    if key.name is None:
        return       
    key.name = key.name.lower()
    if key.event_type == "down":  # When a key is pressed

        if key.name not in keys:
            keys.append(key.name)  # Add to active keys
            command = configure.get_config(" ".join(keys))["command"] if configure.get_config(" ".join(keys)) != None else None
            print(command)
            
            subprocess.run([command], shell=True) if command != None else None



    elif key.event_type == "up" and key.name in keys:
        keys.remove(key.name)  # Remove released key

    print(keys)
while True:
    keyboard.hook(lambda event: search_action(event))
    keyboard.wait()
