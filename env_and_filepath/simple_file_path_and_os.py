# you should run via terminal using python <filename.py> the file path depends on where you run the command in terminal
import json
from pathlib import Path
directory_path = Path.cwd()
print("current path is :", directory_path)