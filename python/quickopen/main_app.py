import asyncio
import logging
from pathlib import Path
from quickopen.listener import Listener
from quickopen.action_handler import ActionHandler

class MainApp:
    def __init__(self, config_file: str | Path):
        """Initialize the MainApp with configuration.
        
        Args:
            config_file: Path to the configuration file
        """
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Convert string path to Path object
        self.config_path = Path(config_file)
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")
        
        self.listener = Listener()
        self.action_handler = ActionHandler(str(self.config_path))
        self.running = True
        self._tasks: list[asyncio.Task] = []

    async def run(self) -> None:
        """Run the main application loop."""
        try:
            # Create tasks for keyboard listening and action handling
            self._tasks = [
                asyncio.create_task(self.keyboard_monitor()),
                asyncio.create_task(self.action_monitor())
            ]
            
            self.logger.info("Starting application...")
            await asyncio.gather(*self._tasks)
            
        except KeyboardInterrupt:
            self.logger.info("Received keyboard interrupt")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}", exc_info=True)
        finally:
            await self.shutdown()


    async def keyboard_monitor(self, stop: str = "alt+esc") -> None:
        """Monitor keyboard events continuously.
        
        Args:
            stop: The key combination to stop monitoring
        """
        try:
            self.logger.info("Started keyboard monitoring...")
            await self.listener.read_hotkey(stop_key=stop, running=self.running)
        except Exception as e:
            self.logger.error(f"Keyboard monitor error: {e}", exc_info=True)
            self.running = False

    # ...existing code...

# ...existing code...

    async def action_monitor(self) -> None:
        """Monitor and execute actions based on detected hotkeys."""
        try:
            self.logger.info("Started action monitoring...")
            while self.running:
                self.logger.info(self.listener.active_keys)
                if self.listener.current_hotkey:  # Only process if there's an active hotkey
                    self.logger.debug(f"Processing hotkey: {self.listener.current_hotkey}")
                    await self.action_handler.run_task_async(self.listener.current_hotkey, self.running)
                await asyncio.sleep(0.1)  # Small delay to prevent CPU overuse
                
        except Exception as e:
            self.logger.error(f"Action monitor error: {e}", exc_info=True)
            self.running = False

    def add_action(self, action: Listener | str, command: str) -> None:
        """Add a new action to the action handler.
        
        Args:
            action: The hotkey combination or Listener object
            command: The command to execute
        """
        try:
            self.action_handler.add_action(action, command)
            self.logger.info(f"Added new action: {action} -> {command}")
        except Exception as e:
            self.logger.error(f"Failed to add action: {e}")
    
    def show_config(self) :
        """Display the current configuration."""
        return self.action_handler.action_config.config

    async def shutdown(self) -> None:
        """Perform cleanup and shutdown tasks."""
        self.running = False
        
        # Cancel all running tasks
        for task in self._tasks:
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        
        self.logger.info("Application shutdown complete")
        
main = MainApp("C:\\Users\\Void\\Google_Drive\\QuickOpen\\python\\quickopen\\module\\actions.json")