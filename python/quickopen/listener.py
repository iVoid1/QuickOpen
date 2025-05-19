from typing import Callable
from keyboard import KeyboardEvent
import keyboard
import asyncio

class Listener:
    def __init__(self):
        self.active_keys: list[str] = []
        self.current_hotkey = ""
        self._hook = None
    
    # --- Core Methods ---
    
    async def read_hotkey_async(self, stop_key: str = "alt+esc", clear: bool = True):
        """Asynchronously read a hotkey until stop_key is pressed."""
        while self.current_hotkey != stop_key:
            if clear:
                self.clear_keys()
            self.current_hotkey = keyboard.read_hotkey()
            await asyncio.sleep(0.1)

    def read_hotkey(self, stop_key: str = "alt+esc", callback: Callable[[], None] | None = None):
        """Read keys until stop_key is pressed."""
        while self.current_hotkey != stop_key:
            keyboard.hook(lambda event: self.handle_event(event, callback))
            keyboard.unhook_all()

    def handle_event(self, event: KeyboardEvent, callback: Callable[[], None] | None = None):
        """Handle a keyboard event."""
        if event.name is None:
            return

        if callback:
            callback()

        if event.event_type == "down":
            if event.name not in self.active_keys:
                self.active_keys.append(event.name)
        elif event.event_type == "up":
            if event.name in self.active_keys:
                self.active_keys.remove(event.name)

        clean_keys = [k for k in self.active_keys if k]
        try:
            self.current_hotkey = keyboard.get_hotkey_name(clean_keys)
            print(self.current_hotkey)
        except ValueError:
            pass

    def clear_keys(self):
        """Clear all active keys and reset the current hotkey."""
        self.active_keys = []
        self.current_hotkey = ""

    # --- Utility Methods ---

    def get_current_keys(self) -> list[str]:
        """Return a copy of the currently held down keys."""
        return self.active_keys.copy()

    async def wait_for_combo(self, combo: str, timeout: float = 10.0) -> bool:
        """Wait for a specific combo to be pressed within a timeout."""
        end_time = asyncio.get_event_loop().time() + timeout
        while asyncio.get_event_loop().time() < end_time:
            await asyncio.sleep(0.05)
        return False

    def block_key(self, key: str):
        """Block a specific key from functioning."""
        keyboard.block_key(key)

    def simulate_keypress(self, key: str):
        """Simulate pressing and releasing a key."""
        keyboard.press_and_release(key)

    def pause_listening(self):
        """Pause keyboard listening."""
        if self._hook:
            keyboard.unhook(self._hook)
            self._hook = None

    def resume_listening(self, callback: Callable[[], None] | None = None):
        """Resume keyboard listening."""
        if not self._hook:
            self._hook = keyboard.hook(lambda event: self.handle_event(event, callback))
