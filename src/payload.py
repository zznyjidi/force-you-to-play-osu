import psutil
import os
from pathlib import Path

home = Path.home()
osu_path = str(home) + r"\AppData\Local\osulazer\current\osu!.exe"

while True:
    if not ('osu!.exe' in (p.name() for p in psutil.process_iter())):
        os.system(osu_path)
