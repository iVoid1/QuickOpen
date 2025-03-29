from pathlib import Path
import os

file = Path(os.path.join(__file__))

print(file.absolute())