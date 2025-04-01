import sys
from pathlib import Path
import subprocess

p = f'"{ sys.executable[0:-4] }w.exe"'
s = fr' { Path.home() }\start.py'
subprocess.Popen(p+s, creationflags=subprocess.DETACHED_PROCESS) # type: ignore

