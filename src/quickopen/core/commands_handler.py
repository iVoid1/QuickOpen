import subprocess
import asyncio
from pathlib import Path

from quickopen.core.logger import log
from quickopen.core.config import Config




class CommandHandler:
    """Handles execution of commands based on hotkey combinations."""
    
    def __init__(self, file_name: str|Path):
        """Initialize the commandHandler with a configuration file."""
        
        self.command_config = Config(str(file_name))
        log.info(f"Initialized commandHandler with config: {file_name}")
        self.shortcut_map = self._build_map()

    def _build_map(self) -> dict[str, str]:
        return {item["shortcut"]: item["command"] for item in self.command_config.config} if self.command_config.config else {}

    def get_command(self, shortcut: str) -> str | None:
        return self.shortcut_map.get(shortcut)
    
    def has_shortcut(self, key, value) -> bool:
        return any(item[key] == value for item in self.command_config.config) if self.command_config.config else False

    async def run_task_async(self, shortcut: str) -> None:
        """Monitor and execute tasks asynchronously.
        
        Args:
            listener: Keyboard listener instance
            running: Control flag for the monitoring loop
        """
        try:
            log.info(shortcut)
            task = self.get_command(shortcut)
            log.info(task) if task is not None else None
            self.run_task(task) if task is not None else None
                
            await asyncio.sleep(0.1)
                
        except Exception as e:
            log.error(f"Error in command monitor: {e}")
            raise e
        
    def run_task(self, command: str) -> bool:
        """Execute a task based on the hotkey combination.
        
        Args:
            combo: Hotkey combination to execute
            
        Returns:
            True if task was executed successfully, False otherwise
        """
        if not self.command_config.config:
            log.warning("No configuration available")
            return False
        
        try:
            subprocess.run(command, shell=True, check=True)
            return True
        
        except subprocess.SubprocessError as e:
            log.error(f"Failed to execute command: {e}")
            return False
            
        return False
    def add_command(self, shortcut: str, command: str) -> bool:
        """Add a new command to the configuration.
        
        Args:
            shortcut: Hotkey combination
            command: Command to execute
            
        Returns:
            True if command was added successfully, False otherwise
        """
        if not self.command_config.config:
            log.warning("No configuration available")
            return False
            
        self.command_config.add_config({"command": command,
                                       "shortcut": shortcut}
                                      )
        
        log.info(f"Added command: {shortcut} -> {command}")
        return True

    def remove_command(self, index:int) -> bool|None:
        """Remove an command from the configuration.
        
        Args:
            keys: Hotkey combination or Listener instance to remove
            
        Returns:
            True if command was removed successfully, False otherwise
        """
        if not self.command_config.config:
            log.warning("No configuration available")
            return False
            
        item = self.command_config.remove_config(index)
        log.info(f"Removed command: {index}")
        return item
    
    def update_command(self, index:int, new_shortcut:str, command:str|None = None):
        if self.command_config.config == None:
            return
        
        self.command_config.update_config(
            keys=index,
            new_value={
                "command": command,
                "shortcut": new_shortcut
            }
        )
            