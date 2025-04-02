import subprocess
from module.config import Config
from key_reader import KeyReader



class ActionHandler:
    
    def __init__(self, file_name:str):
        self.action_config = Config(file_name)
    
    def run_action(self, keys_on_press:KeyReader):
        subprocess.run([self.action_config.get_config(keys_on_press.pressed)["command"]], shell=True)

    def add_action(self, shortcut:KeyReader,name:str , command:str):
        if self.action_config.config == None:
            print("No config found")
            return None
        
        self.action_config.add_config(shortcut.active_keys, 
                                      {"id":len(self.action_config.config) + 1,
                                       "name":name,
                                       "command":command
                                       }
                                      )
    
    def remove_action(self, keys_on_press:KeyReader):
        return self.action_config.remove_config(keys_on_press.pressed)

    def update_action(self, old_keys_on_press:KeyReader, new_keys_on_press:KeyReader, name:str | None = None, command:str | None = None):
        if self.action_config.config == None:
            print("No config found")
            return None
        
        self.action_config.update_config(
            keys=old_keys_on_press, 
            new_key=new_keys_on_press, 
            new_value={"id":len(self.action_config.config) + 1, 
                       "name":name, 
                       "command":command}
            )

    def merge_actions(self):
        pass

    def load_actions(self):
        pass


    def get_actions(self):
        pass
