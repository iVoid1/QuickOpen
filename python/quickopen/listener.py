from typing import Callable
from keyboard import KeyboardEvent
import keyboard
import asyncio

class Listener:
    def __init__(self):
        self.last_key = ""
        self.pressed = []
        self.active_keys = []
        self.active_keys_str = ""
        self.init = False
        self.hook = None

    # --- Core Methods ---
    
    def read_hotkey(self) -> str:
        """Read a hotkey from the user"""
        self.hotkeys = keyboard.read_hotkey()
        return self.hotkeys

    async def read_key(self, stop_key: str = "alt+esc", func: Callable[[], None] | None = None):
        """Reads keys asynchronously until stop_key is pressed."""
        if not self.init:
            self.clear()
            self.init = True

        print("Started listening...")

        # Set up a single persistent hook
        self.hook = keyboard.hook(lambda event: self.on_key_event(event, func))

        try:
            while "+".join(self.active_keys_str) != stop_key:
                await asyncio.sleep(0.05)
        finally:
            keyboard.unhook(self.hook)
            print("Stopping key reader...")

    def on_key_event(self, key_event: KeyboardEvent, func: Callable[[], None] | None):
        """Handles key events."""
        if key_event.name is None:
            return

        if func is not None:
            func()

        if key_event.event_type == "down":
            self.last_key = key_event.name
            self.pressed.append(key_event.name)

            if key_event.name not in self.active_keys:
                self.active_keys.append(key_event.name)
                self.active_keys_str = "+".join(self.active_keys)

        elif key_event.event_type == "up":
            if key_event.name in self.active_keys:
                self.active_keys.remove(key_event.name)
                self.active_keys_str = "+".join(self.active_keys)

    def clear(self):
        self.last_key = ""
        self.pressed = []
        self.active_keys = []
        self.active_keys_str = ""

     # --- Utility / Future Methods ---

    def was_key_pressed(self, key: str) -> bool:
        """Check if a key was pressed during session."""
        return key in self.pressed

    def get_active_keys(self) -> list[str]:
        """Return currently held down keys."""
        return self.active_keys.copy()

    async def wait_for_combo(self, combo: str, timeout: float = 10.0) -> bool:
        """Wait for a combo to be pressed within a timeout."""
        print(f"Waiting for {combo} for {timeout} seconds...")
        end_time = asyncio.get_event_loop().time() + timeout
        while asyncio.get_event_loop().time() < end_time:
            if self.active_keys_str == combo:
                return True
            await asyncio.sleep(0.05)
        return False

    def block_key(self, key: str):
        """Block a specific key from functioning."""
        keyboard.block_key(key)

    def simulate_keypress(self, key: str):
        """Simulate pressing and releasing a key."""
        keyboard.press_and_release(key)

    def get_combo_history(self) -> list[str]:
        """Return a list of combos that were pressed."""
        combos = []
        combo = []
        for key in self.pressed:
            combo.append(key)
            if len(combo) > 1:
                combos.append("+".join(combo))
        return combos

    def pause_listening(self):
        """Temporarily pause keyboard listening."""
        if self.hook:
            keyboard.unhook(self.hook)
            self.hook = None
            print("Listener paused.")

    def resume_listening(self, func: Callable[[], None] | None = None):
        """Resume keyboard listening."""
        if not self.hook:
            self.hook = keyboard.hook(lambda event: self.on_key_event(event, func))
            print("Listener resumed.")