import json
from pathlib import Path
import subprocess


class Config:
    def __init__(self, file_name:Path|str = "config.json"):
        self.file_name = file_name
        self.config: dict[str, str]|None = self.load_config()
        
    def load_config(self) -> dict[str, str]|None:
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
            
        except FileNotFoundError:
            print(f"Config file {self.file_name} not found. Create a new one!")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding {self.file_name}. Using an empty config.")
            return None
        

    def get_config(self, keys: str) -> str|None:
        
        if self.config == None:
            return None
        
        action_file = self.config.get(keys)
        
        if action_file:
            subprocess.run(["python", action_file]) if action_file.endswith(".py") else None
            subprocess.run([action_file]) if action_file.endswith(".exe") or action_file.endswith(".bat") else print(f"Unsupported file type: {action_file}")
            return action_file
        
        print(f"Action file '{action_file}' not found.")
        return None
                
        
    def add_config(self, keys:str, action:str) -> dict[str, str]|None:
        if self.config == None:
            return None
        
        self.config[keys] = action
        self.save_config()
        return {keys:action}
    
    def save_config(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.config, file, indent=4)
    
    def remove_config(self, keys:str) -> bool|None:
        if self.config == None:
            return None
        
        if keys in self.config:
            del self.config[keys]
            self.save_config()
            return True
        return False

