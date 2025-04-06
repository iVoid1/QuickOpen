from typing import Callable
from keyboard import KeyboardEvent
import keyboard
from pynput.keyboard import Key, KeyCode
import asyncio

class KeyReader:
    @staticmethod
    def get_key(key: Key | KeyCode | str) -> str | None:
        return key.name if isinstance(key, Key) else key.char if isinstance(key, KeyCode) else key or None

    def __init__(self):
        self.last_key: str = ""
        self.pressed: list[str] = []
        self.active_keys: list[str] = []  # Track currently pressed keys
        self.active_keys_str: str = ""
        self.init: bool = False

    async def read_key(self, stop_key: Key | KeyCode | str = "esc", func: Callable[[], None] | None = None):
        """Reads keys asynchronously until stop_key is pressed."""

        key = self.get_key(stop_key)
        if key is None:
            return
        
        # Initialize if not already done
        if not self.init:
            self.clear()
            self.init = True

        # Hook into all keyboard events
        keyboard.hook(lambda event: self.on_key_event(event, func))
        try:
            while self.last_key != key:
                await asyncio.sleep(0.1)  # Allow event loop to run
                
        except:
            pass

        finally:
            keyboard.unhook_all()

        print("Stopping key reader...")

    def on_key_event(self, key_event: KeyboardEvent, func: Callable[[], None] | None):
        """Handles key events."""
        if key_event.name is None:
            return

        if func is not None:
            func()  # Call the provided function on key event        

        if key_event.event_type == "down":  # When a key is pressed
            self.last_key = key_event.name  # Store the key pressed
            self.pressed.append(key_event.name)  # Track all pressed keys

            if key_event.name not in self.active_keys:
                self.active_keys.append(key_event.name)  # Add to active keys

            self.active_keys_str += key_event.name

        elif key_event.event_type == "up" and key_event.name in self.active_keys:
            self.active_keys.remove(key_event.name)  # Remove released key

    def clear(self):
        """Clears all stored keys."""
        self.last_key = ""
        self.pressed = []
        self.active_keys = []
        self.active_keys_str = ""

    def is_key_pressed(self, key: Key | KeyCode | str) -> bool:
        """Checks if a key is currently pressed."""
        return self.get_key(key) in self.active_keys
