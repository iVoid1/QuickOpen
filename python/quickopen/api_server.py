from fastapi import FastAPI, HTTPException
from typing import Dict
import uvicorn
from quickopen.main_app import MainApp

app = FastAPI()

# Initialize MainApp with the path to the configuration file
config_path = "python/quickopen/module/actions.json"
main_app = MainApp(config_path)

@app.get("/actions", response_model=Dict[str, str])
async def get_actions():
    """Retrieve all configured actions."""
    return main_app.action_handler.action_config.config

@app.post("/actions")
async def add_action(shortcut: str, command: str):
    """Add a new action."""
    success = main_app.action_handler.add_action(shortcut, command)
    if success:
        return {"message": "Action added successfully"}
    raise HTTPException(status_code=400, detail="Failed to add action")

@app.delete("/actions/{shortcut}")
async def remove_action(shortcut: str):
    """Remove an action."""
    index = main_app.action_handler.action_config.index_config(shortcut)
    if index is not None:
        success = main_app.action_handler.remove_action(index)
        if success:
            return {"message": "Action removed successfully"}
    raise HTTPException(status_code=404, detail="Action not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

