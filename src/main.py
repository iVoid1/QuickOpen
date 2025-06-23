from quickopen.core.logger import log
from quickopen.app import MainApp
import asyncio
import threading

main_app = MainApp("C:\\Users\\Void\\Google_Drive\\projects\\QuickOpen\\src\\data\\actions.json")

def main():
    log.info("Starting API server...")

    # نشغل Flask في ثريد منفصل
    api_thread = threading.Thread(target=main_app.Server.run, daemon=True)
    api_thread.start()
    
    log.info("Starting main app...")
    asyncio.run(main_app.run())
if __name__ == "__main__":
    main()