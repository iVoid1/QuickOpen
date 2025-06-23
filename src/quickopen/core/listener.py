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
                self.active_keys.append(event.name.lower())
                
                self.active_keys = self.sort_keys(self.active_keys)
                self.current_hotkey = " ".join(self.active_keys)
                print(event.scan_code)        
                
                                
            elif event.event_type == "up" and event.name in self.active_keys:
                self.active_keys.remove(event.name)
                self.current_hotkey = " ".join(self.active_keys)
                
        except ValueError as e:
            self.logger.error(f"Error processing keyboard event: {e}")

    def sort_keys(self, keys) -> list[str]:
        """Sort keys according to preferred order.
        
        Returns:
            Sorted key combination as string
        """
        combo_set = set(keys)
        ordered = [key for key in self._preferred_order if key in combo_set]
        rest = sorted(combo_set - set(self._preferred_order))
        return ordered + rest
        

    def clear_keys(self) -> None:
        """Reset active keys and current hotkey."""
        self.active_keys.clear()
        self.current_hotkey = ""
        
def main():
    if __name__ == "__main__":
        listener = Listener()
        while True:
            keyboard.hook(listener.handle_event)
main()        
