from QuickOpen.python.quickopen.listener import Listener
from action_handler import ActionHandler
import asyncio



class MainApp:
    def __init__(self, config_file: str):
        self.listener = Listener()
        self.action_handler = ActionHandler(config_file)

    async def run(self):
        
        print("Starting QuickOpen...")
        
        self.action_handler.add_action(self.listener, "VS Code", "code")
        self.action_handler.run_task(self.listener.read_hotkey())

        


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(MainApp(r"C:\Users\Void\Google_Drive\QuickOpen\QuickOpen\python\quickopen\module\actions.json").run())