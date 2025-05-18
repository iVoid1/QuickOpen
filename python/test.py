import keyboard
from typing import Callable, Dict
from quickopen.module.config import Config 
import subprocess
config = Config(r"C:\Users\Void\Google_Drive\QuickOpen\QuickOpen\python\quickopen\module\actions.json")

class HotkeyManager:
    def __init__(self, config_file: Config = config):
        self.actions: Config = config_file
        self.hotkeys = ""
    def read_hotkey(self) -> str:
        """Read a hotkey from the user"""
        self.hotkeys = keyboard.read_hotkey()
        return self.hotkeys
    
    def run_task(self, combo: str) -> None:
        """Add a new hotkey with its callback function"""
        if combo in self.actions.config:
            subprocess.run([self.actions.get_config(combo)['command']], shell=True)
        
    def remove_hotkey(self, combo: str) -> None:
        """Remove a hotkey"""
        if combo in self.actions:
            keyboard.remove_hotkey(combo)
            del self.actions[combo]

    def clear_all_hotkeys(self) -> None:
        """Remove all registered hotkeys"""
        for combo in list(self.actions.keys()):
            self.remove_hotkey(combo)
            
    def add_hotkey(self, combo: str, func: Callable[[], None]) -> None:
        """Add a new hotkey with its callback function"""
        keyboard.add_hotkey(combo, func)

def main():
    manager = HotkeyManager()
    combo = keyboard.read_hotkey()
    manager.add_hotkey(combo, )

if __name__ == "__main__":
    # main()
    pass
combo = keyboard.read_hotkey()
print(combo)