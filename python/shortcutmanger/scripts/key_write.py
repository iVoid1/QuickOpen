import os
import re

def make_file(path: str|None = None,
              file_name: str = "file",
              copy: bool = True,
              open_file: bool = False,
              file_type: str = "txt",
              text: str = "",
              mode: str = "x",
              return_option: str = 'path',
              read_only: bool = False):
    
    """ 
    Create or manipulate a file at the specified path. 
    Mode: 
        'r' -> read only, 'w' -> write, 'a' -> append, 'x' -> create new.
    Return options:
        'path' -> file path, 'read' -> file content.
    """
    if path == None:
        path = os.path.dirname(os.path.abspath(__file__))
        
    path = path.rstrip()
    
    if not os.path.exists(path):
        return "Error: Specified folder path does not exist."

    # File creation
    path_file = os.path.join(path, f"{file_name}.{file_type}")
    if copy:
        count = 2
        while os.path.exists(path_file):
            file_name = re.sub(r"\(\d+\)$", "", file_name) + f"({count})"
            path_file = os.path.join(path, f"{file_name}.{file_type}")
            count += 1

    # Adjust mode for read-only
    if read_only:
        mode = 'r'

    # Open file and perform operation
    with open(path_file, mode=mode) as file:
        content = ""
        if mode in ["w", "a", "x", "w+", "a+", "x+"]:
            file.write(text)
        if mode in ["r", "r+", 'w+', 'a+', 'x+']:
            file.seek(0)  # Read content if mode permits
            content = file.read()

    if open_file:
        os.startfile(path_file)

    # Return based on user choice
    if return_option == "read":
        return content
    return path_file
