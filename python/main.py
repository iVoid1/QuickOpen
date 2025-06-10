from quickopen.api_server import app
import logging
import asyncio
import threading
from quickopen.main_app import main

logger = logging.getLogger(__name__)

def run_api_server():
    app.run(port=4000)


async def run():
    logger.info("Starting API server...")

    # نشغل Flask في ثريد منفصل
    api_thread = threading.Thread(target=run_api_server, daemon=True)
    api_thread.start()

    logger.info("Starting main app...")
    await main.run()

if __name__ == "__main__":
    asyncio.run(run())
    