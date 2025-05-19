from listener import Listener
from action_handler import ActionHandler
import asyncio
import keyboard

class MainApp:
    def __init__(self, config_file: str):
        self.listener = Listener()
        self.action_handler = ActionHandler(config_file)
        self.running = True

    async def run(self):
        # Create tasks for keyboard listening and action handling
        keyboard_task = asyncio.create_task(self.keyboard_monitor())
        action_task = asyncio.create_task(self.action_monitor())
        
        try:
            # Wait for both tasks
            await asyncio.gather(keyboard_task, action_task)
        except KeyboardInterrupt:
            self.running = False

    async def keyboard_monitor(self, stop: str = "alt+esc"):
        """Monitor keyboard events continuously"""
        print("Started keyboard monitoring...")
        keyboard.hook(self.listener.handle_event)
        
        try:
            while self.running:
                if keyboard.is_pressed(stop):  # Emergency exit
                    self.running = False
                    break
                await asyncio.sleep(0.1)
        finally:
            keyboard.unhook_all()
            print("Keyboard monitoring stopped.")

    async def action_monitor(self):
        """Monitor and execute actions based on detected hotkeys"""
        print("Started action monitoring...")
        try:
            while self.running:
                if self.listener.current_hotkey:
                    self.action_handler.run_task(self.listener.current_hotkey)
                await asyncio.sleep(0.1)
        except Exception as e:
            print(f"Error in action monitor: {e}")
            self.running = False

if __name__ == "__main__":
    app = MainApp(r"C:\Users\Void\Google_Drive\QuickOpen\python\quickopen\module\actions.json")
    asyncio.run(app.run())