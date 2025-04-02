from action_handler import ActionHandler
from key_reader import KeyReader
import asyncio

async def main() -> None:
    actions = ActionHandler("module\\actions.json")
    keys = KeyReader()
    await keys.read_key(stop_key="esc", func=lambda:print(" ".join(keys.active_keys)))
    actions.run_action(keys)
if __name__ == "__main__":    
    asyncio.run(main())
