import asyncio
from pathlib import Path
from quickopen.core.listener import Listener
from quickopen.core.commands_handler import CommandHandler
from quickopen.api.server import Server
from quickopen.core.logger import log



class MainApp:
    def __init__(self, config_file: str|Path):
        """Initialize the MainApp with configuration.
        
        Args:
            config_file: Path to the configuration file
        """
        self.running = True
        self._tasks: list[asyncio.Task] = []
        self.listener = Listener()
        self.command_handler = CommandHandler(str(config_file))
        self.Server = Server(self.command_handler)
        
    async def run(self) -> None:
        """Run the main application loop."""
        try:
            # Create tasks for keyboard listening and command handling
            self._tasks = [
                asyncio.create_task(self.keyboard_monitor()),
                asyncio.create_task(self.command_monitor())
            ]
                
            log.info("Starting application...")
            await asyncio.gather(*self._tasks)
            
        except KeyboardInterrupt:
            log.info("Received keyboard interrupt")
        except Exception as e:
            log.error(f"Unexpected error: {e}", exc_info=True)
        finally:
            await self.shutdown()


    async def keyboard_monitor(self, stop: str = "alt+esc") -> None:
        """Monitor keyboard events continuously.
        
        Args:
            stop: The key combination to stop monitoring
        """
        try:
            log.info("Started keyboard monitoring...")
            await self.listener.read_hotkey(stop_key=stop, running=self.running)
        except Exception as e:
            log.error(f"Keyboard monitor error: {e}", exc_info=True)
            self.running = False

    # ...existing code...

# ...existing code...

    async def command_monitor(self) -> None:
        """Monitor and execute commands based on detected hotkeys."""
        try:
            log.info("Started command monitoring...")
            while self.running:
                log.info(self.listener.active_keys)
                if self.listener.current_hotkey:  # Only process if there's an active hotkey
                    log.debug(f"Processing hotkey: {self.listener.current_hotkey}")
                    await self.command_handler.run_task_async(self.listener.current_hotkey)
                await asyncio.sleep(0.1)  # Small delay to prevent CPU overuse
                
        except Exception as e:
            log.error(f"command monitor error: {e}", exc_info=True)
            self.running = False

    def add_command(self, shortcut: str, command: str) -> None:
        """Add a new command to the command handler.
        
        Args:
            command: The hotkey combination or Listener object
            command: The command to execute
        """
        try:
            self.command_handler.add_command(command, command)
            log.info(f"Added new command: {command} -> {command}")
        except Exception as e:
            log.error(f"Failed to add command: {e}")
    
    def show_config(self) :
        """Display the current configuration."""
        return self.command_handler.command_config.config

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
        
        log.info("Application shutdown complete")
        
