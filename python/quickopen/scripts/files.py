from pathlib import Path
import os

file = Path(os.path.join(__file__))
file.replace("files")
print(file)