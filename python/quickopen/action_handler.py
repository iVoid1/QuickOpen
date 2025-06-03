import logging
import subprocess
from typing import Optional, Union
from pathlib import Path
from quickopen.module.config import Config
from quickopen.listener import Listener
import asyncio


class ActionHandler:
    """Handles execution of actions based on hotkey combinations."""
    
    def __init__(self, file_name: Union[str, Path]):
        self.logger = logging.getLogger(__name__)
        self.action_config = Config(str(file_name))
        self.logger.info(f"Initialized ActionHandler with config: {file_name}")

    def run_task(self, combo: str) -> bool:
        """Execute a task based on the hotkey combination.
        
        Args:
            combo: Hotkey combination to execute
            
        Returns:
            True if task was executed successfully, False otherwise
        """
        if not self.action_config.config:
            self.logger.warning("No configuration available")
            return False
            
        if combo in self.action_config.config:
            try:
                command = self.action_config.get_config(combo)
                subprocess.run(command, shell=True, check=True)
                self.logger.info(f"Executed command: {command}")
                return True
            except subprocess.SubprocessError as e:
                self.logger.error(f"Failed to execute command: {e}")
                return False
        return False

    async def run_task_async(self, listener: Listener, running: bool) -> None:
        """Monitor and execute tasks asynchronously.
        
        Args:
            listener: Keyboard listener instance
            running: Control flag for the monitoring loop
        """
        self.logger.info("Starting ActionHandler monitor...")
        try:
            while running:
                if listener.current_hotkey:
                    self.run_task(listener.current_hotkey)
                await asyncio.sleep(0.1)
        except Exception as e:
            self.logger.error(f"Error in action monitor: {e}")
            raise
        finally:
            self.logger.info("Action monitor stopped")

    def add_action(self, shortcut: Union[Listener, str], command: str) -> bool:
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
        self.action_config.add_config(key, command)
        self.logger.info(f"Added action: {key} -> {command}")
        return True

    def remove_action(self, keys: Union[Listener, str]) -> bool|None:
        """Remove an action from the configuration.
        
        Args:
            keys: Hotkey combination or Listener instance to remove
            
        Returns:
            True if action was removed successfully, False otherwise
        """
        if not self.action_config.config:
            self.logger.warning("No configuration available")
            return False
            
        key = keys if isinstance(keys, str) else keys.current_hotkey
        result = self.action_config.remove_config(key)
        if result:
            self.logger.info(f"Removed action: {key}")
        return result

    def update_action(self, old_keys_on_press:Listener|str, new_keys_on_press:Listener|str, name:str | None = None, command:str | None = None):
        if self.action_config.config == None:
            return
        
        self.action_config.update_config(
            keys=old_keys_on_press, 
            new_key=new_keys_on_press, 
            new_value=command
        )
