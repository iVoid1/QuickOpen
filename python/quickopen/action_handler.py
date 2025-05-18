import subprocess
from module.config import Config
from QuickOpen.python.quickopen.listener import Listener



class ActionHandler:
    
    def __init__(self, file_name:str):
        self.action_config = Config(file_name)
    
    def run_task(self, combo: str) -> None:
        """Add a new hotkey with its callback function"""
        if combo in self.action_config.config:
            subprocess.run([self.action_config.get_config(combo)['command']], shell=True)
        return
    
    def add_action(self, shortcut:Listener, name:str, command:str):
        if not self.chuck_actions():
            return None
        shortcut.read_hotkey()
        self.action_config.add_config(shortcut.hotkeys, 
                                      {"id":len(self.action_config.config) + 1,
                                       "name":name,
                                       "command":command
                                       }
                                      )
    
    def remove_action(self, keys_on_press:Listener):
        if not self.chuck_actions():
            return None
        return self.action_config.remove_config(keys_on_press.pressed)

    def update_action(self, old_keys_on_press:Listener, new_keys_on_press:Listener, name:str | None = None, command:str | None = None):
        if not self.chuck_actions():
            return None
        
        self.action_config.update_config(
            keys=old_keys_on_press, 
            new_key=new_keys_on_press, 
            new_value={"id":len(self.action_config.config) + 1, 
                       "name":name, 
                       "command":command}
            )
        
        self.action_config.save_config()


    def chuck_actions(self):
        if self.action_config.config == None:
            print("No config found")
            return False
        return True