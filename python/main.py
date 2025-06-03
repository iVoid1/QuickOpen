from quickopen.main_app import MainApp
from pathlib import Path
import asyncio


config_path = Path("C:\\Users\\Void\\Google_Drive\\QuickOpen\\python\\quickopen\\module\\actions.json")
app = MainApp(config_path)
asyncio.run(app.run())