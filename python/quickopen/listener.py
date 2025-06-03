import logging
from typing import Callable, Optional, List
from keyboard import KeyboardEvent
import keyboard
import asyncio

class Listener:
    """Handles keyboard event listening and hotkey detection."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.active_keys: List[str] = []
        self.current_hotkey: str = ""
        self._hook: Optional[Callable] = None
        self._preferred_order = ["ctrl", "shift", "alt", "cmd", "win"]

    async def read_hotkey(self, running: bool, stop_key: str = "alt esc") -> None:
        """Read keys until stop_key is pressed.
        
        Args:
            running: Control flag for the listening loop
            stop_key: Key combination to stop listening
        """
        self.logger.info("Starting Listener...")
        self.clear_keys()
        keyboard.hook(self.handle_event)
        
        try:
            self.logger.info("Listening for hotkeys...")
            while running:
                if keyboard.is_pressed(stop_key):
                    self.logger.info("Stop key pressed, ending listener")
                    break
                await asyncio.sleep(0.1)
        finally:
            keyboard.unhook_all()
            self.logger.info("Keyboard monitoring stopped")

    def handle_event(self, event: KeyboardEvent) -> None:
        """Process keyboard events and update active keys.
        
        Args:
            event: Keyboard event to process
        """
        if not event.name:
            return

        try:
            if event.event_type == "down" and event.name not in self.active_keys:
                self.active_keys.append(event.name)
                self.current_hotkey = self.sort_keys()
                self.logger.debug(f"Key pressed: {self.current_hotkey}")
                
            elif event.event_type == "up" and event.name in self.active_keys:
                self.active_keys.remove(event.name)
                self.current_hotkey = self.sort_keys()

            self.logger.debug(f"Active keys: {self.active_keys}")
            self.logger.debug(f"Current hotkey: {self.current_hotkey}")
        except ValueError as e:
            self.logger.error(f"Error processing keyboard event: {e}")

    def sort_keys(self) -> str:
        """Sort keys according to preferred order.
        
        Returns:
            Sorted key combination as string
        """
        combo_set = set(self.active_keys)
        ordered = [key for key in self._preferred_order if key in combo_set]
        rest = sorted(combo_set - set(self._preferred_order))
        self.active_keys = ordered + rest
        return ' '.join(self.active_keys)

    def clear_keys(self) -> None:
        """Reset active keys and current hotkey."""
        self.active_keys.clear()
        self.current_hotkey = ""

    def block_key(self, key: str) -> None:
        """Block a specific key from functioning.
        
        Args:
            key: Key to block
        """
        keyboard.block_key(key)
        self.logger.debug(f"Blocked key: {key}")

    def toggle_listening(self, enable: bool) -> None:
        """Toggle keyboard listening on/off.
        
        Args:
            enable: True to enable listening, False to disable
        """
        if enable and not self._hook:
            self._hook = keyboard.hook(self.handle_event)
            self.logger.info("Keyboard listening enabled")
        elif not enable and self._hook:
            keyboard.unhook(self._hook)
            self._hook = None
            self.logger.info("Keyboard listening disabled")