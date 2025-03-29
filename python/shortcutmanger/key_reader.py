from pathlib import Path
from keyboard import KeyboardEvent
import keyboard
from pynput.keyboard import Key, KeyCode
from module.config import Config

class KeyReader:
    
    def __init__(self, config_file:Path|str = "module\\config.json",):
        self.last_pressed_key:str = ""
        self.pressed_keys_list:list[str] = []
        self.currently_pressed_keys:list[str] = []  # Track currently pressed keys
        
        self.is_initialized:bool = False
        self.config_file: Path|str = config_file
        
    def read_key(self, target_key: Key | KeyCode | str = "esc"):
        
        keyboard.hook(self.on_key_event)  # Hook into all keyboard events
        while self.last_pressed_key != target_key:            
            try:
                if isinstance(target_key, Key):
                    keyboard.wait(target_key.name)
                    break
                if isinstance(target_key, KeyCode):
                    keyboard.wait(target_key.char)
                    break 
                keyboard.wait(target_key)
                break
            except KeyboardInterrupt:
                pass
    def on_key_event(self, key_event:KeyboardEvent):
        if key_event.name != None:
            if key_event.event_type == "down":  # When a key is pressed
                self.last_pressed_key = key_event.name  # Store the key pressed

                if key_event.name not in self.currently_pressed_keys:  # Avoid duplicates
                    self.pressed_keys_list.append(key_event.name)  # Track all pressed keys
                    self.currently_pressed_keys.append(key_event.name)  # Add to active keys list
                    config = Config(self.config_file)
                    config.get_config(" ".join(self.currently_pressed_keys))
            elif key_event.event_type == "up" and key_event.name in self.currently_pressed_keys:  
                # When a key is released, remove it from the active keys list
                self.currently_pressed_keys.remove(key_event.name)
            
def main() -> None:
    if __name__ == "__main__":
        key_reader = KeyReader()
        key_reader.read_key("esc")

main()
