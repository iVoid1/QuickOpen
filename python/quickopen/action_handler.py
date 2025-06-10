import logging
import subprocess
from pathlib import Path
from quickopen.module.config import Config
from quickopen.listener import Listener
import asyncio




class ActionHandler:
    """Handles execution of actions based on hotkey combinations."""
    
    def __init__(self, file_name: str|Path):
        self.logger = logging.getLogger(__name__)
        self.action_config = Config(str(file_name))
        self.logger.info(f"Initialized ActionHandler with config: {file_name}")
        self.shortcut_map = self._build_map()

    def _build_map(self) -> dict[str, str]:
        return {item["shortcut"]: item["action"] for item in self.action_config.config} if self.action_config.config else {}

    def get_action(self, shortcut: str) -> str | None:
        return self.shortcut_map.get(shortcut)
    
    def has_shortcut(self, key, value) -> bool:
        return any(item[key] == value for item in self.action_config.config) if self.action_config.config else False

    async def run_task_async(self, shortcut: str, running: bool) -> None:
        """Monitor and execute tasks asynchronously.
        
        Args:
            listener: Keyboard listener instance
            running: Control flag for the monitoring loop
        """
        try:
            self.logger.info(shortcut)
            task = self.get_action(shortcut)
            self.logger.info(task) if task is not None else None
            self.run_task(task) if task is not None else None
                
            await asyncio.sleep(0.1)
                
        except Exception as e:
            self.logger.error(f"Error in action monitor: {e}")
            raise e
        
    def run_task(self, command: str) -> bool:
        """Execute a task based on the hotkey combination.
        
        Args:
            combo: Hotkey combination to execute
            
        Returns:
            True if task was executed successfully, False otherwise
        """
        if not self.action_config.config:
            self.logger.warning("No configuration available")
            return False
        
        try:
            subprocess.run(command, shell=True, check=True)
            return True
        
        except subprocess.SubprocessError as e:
            self.logger.error(f"Failed to execute command: {e}")
            return False
            
        return False
    def add_action(self, shortcut: str|Listener, command: str) -> bool:
        """Add a new action to the configuration.
        
        Args:
            shortcut: Hotkey combination or Listener instance
            command: Command to execute
            
        Returns:
            True if action was added successfully, False otherwise
        """
        if not self.action_config.config:
            self.logger.warning("No configuration available")
            return False
            
        key = shortcut if isinstance(shortcut, str) else shortcut.current_hotkey
        self.action_config.add_config({"action": command,
                                       "shortcut": key}
                                      )
        
        self.logger.info(f"Added action: {key} -> {command}")
        return True

    def remove_action(self, index:int) -> bool|None:
        """Remove an action from the configuration.
        
        Args:
            keys: Hotkey combination or Listener instance to remove
            
        Returns:
            True if action was removed successfully, False otherwise
        """
        if not self.action_config.config:
            self.logger.warning("No configuration available")
            return False
            
        item = self.action_config.remove_config(index)
        self.logger.info(f"Removed action: {index}")
        return item
    
    def update_action(self, index:int, new_shortcut:str, command:str|None = None):
        if self.action_config.config == None:
            return
        
        self.action_config.update_config(
            keys=index,
            new_value={
                "action": command,
                "shortcut": new_shortcut
            }
        )
            
