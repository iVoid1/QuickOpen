import json
import typing
import logging
from pathlib import Path
from typing import Any, Union, Dict, List




class Config:
    """A class for managing configuration files."""
    @staticmethod
    def get_item(List:list[Any]|None, index:int) -> Any|None:
        return List[index] if List != None and index < len(List) and index >= -len(List) else None
    
    @staticmethod
    def get_index(List:list[Any]|None, value:Any) -> int|None:
        return List.index(value) if List != None and value in List else None

    def __init__(self, file_name: Union[str, Path], config_type: type = dict, auto_save: bool = True):
        """Initializes the Config object, loading the config file if it exists.

        Args:
            file_name: Path to configuration file
            config_type: Expected type of configuration (dict or list)
            auto_save: Whether to automatically save changes
        """

        self.logger = logging.getLogger(__name__)
        self.file_name = Path(file_name)
        if not self.file_name.suffix:
            self.file_name = self.file_name.with_suffix('.json')
            
        self.type = config_type
        self.auto_save = auto_save
        self.config = self.load_config()
        
        
    def load_config(self) -> Dict[Any, Any]|List[Any]|None:
        """Loads the configuration from the file.

        Returns:
            Configuration data or None if loading fails
        """

        try:
            with self.file_name.open('r') as file:
                return json.load(file)
                
            
        except FileNotFoundError:
            self.logger.error(f"Config file not found: {self.file_name}")
            return None
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON in config file: {self.file_name}")
            return None

    def get_config(self, key_index:Any|int, default:Any = None) -> Any:
        """Retrieves a value from the config using a key (for dicts) or index (for lists)."""
        if isinstance(self.config, dict) and key_index in self.config:
            return self.config.get(key_index, default)
        
        if isinstance(self.config, list) and isinstance(key_index, int):
            return self.get_item(self.config, key_index)
        
        return default
    
    def index_config(self, keys:Any, default:Any = None) -> int|Any|None:
        """Finds the index of a key in a dict or value in a list."""
        if isinstance(self.config, dict):
            return next((item[0] for item in enumerate(self.config) if item[1] == keys), default)
        
        if keys in self.config:
            return self.get_index(self.config, keys)
        return default
    
    def save_config(self) -> bool:
        """Saves the config to the file."""
        if not self.config:
            return False
            
        try:
            with self.file_name.open('w') as file:
                json.dump(self.config, file, indent=4)
            return True
        except Exception as e:
            self.logger.error(f"Failed to save config: {e}")
            return False

    def add_config(self, keys:Any, value:Any = None):
        """Adds a key-value pair (for dicts) or appends a value (for lists)."""
        if self.config == None:
            print("No config found")
            return None
        
        if isinstance(self.config, dict) :
            self.config[keys] = value
            self.save_config() if self.auto_save else None
            return {keys:value} 

        self.config.append(keys)
        self.save_config() if self.auto_save else None
        return keys

    def remove_config(self, key_or_index:Any|int) -> bool|None:
        """Removes a key (for dicts) or index (for lists)."""
        if isinstance(self.config, dict):
            if key_or_index in self.config:
                self.config.pop(key_or_index)
                self.save_config() if self.auto_save else None
                return True
            
        if isinstance(self.config, list) and isinstance(key_or_index, int) and key_or_index < len(self.config) and key_or_index >= -len(self.config):
            self.config.pop(key_or_index)
            self.save_config() if self.auto_save else None
            return True
        return False

    def update_config(self, keys: Any|int, new_value:Any|None = None, new_key:Any|None = None) -> bool|None:
        """Updates a key's value (for dicts) or replaces an index (for lists)."""
        if self.config == None:
            print("No config found")
            return None
        
        if isinstance(self.config, dict) and keys in self.config:
            if new_value != None:
                self.config[keys] = new_value
            
            if new_key != None:
                self.config[new_key] = self.config.pop(keys)
                
            self.save_config() if self.auto_save else None
            return True
        
        if isinstance(self.config, list) and (keys < len(self.config) or keys >= -len(self.config)):
            self.config.pop(keys)
            self.config.insert(keys, new_value)
            self.save_config() if self.auto_save else None
            return True
        
        return False
    
    def merge_configs(self, other_config: object|dict[Any, Any]|list[Any]):
        """Merges another configuration into the current one."""
        if isinstance(other_config, Config):
            other_config = other_config.config
        
        if isinstance(self.config, dict) and isinstance(other_config, dict):
            for key, value in typing.cast(dict[Any, Any], other_config.items()):
                if key in self.config and isinstance(self.config[key], list) and isinstance(value, list):
                    self.config[key].extend(value)
                else:
                    self.config[key] = value    
            return self.config
        elif isinstance(self.config, list) and isinstance(other_config, list):
            self.config.extend(typing.cast(list[Any], other_config))
        else:
            return None
        self.save_config() if self.auto_save else None
        return self.config
    
    def items(self) -> list[Any]|None:
        if self.config == None:
            return None
        return list(self.config.items()) if isinstance(self.config, dict) else self.config