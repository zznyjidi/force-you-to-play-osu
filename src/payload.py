# Compilation mode, support OS-specific options
# nuitka-project-if: {OS} in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --onefile
# nuitka-project-else:
#    nuitka-project: --mode=standalonealone
# nuitka-project: --windows-console-mode=disable
# nuitka-project: --include-package-data=psutil

import psutil
import os
import urllib.request
from pathlib import Path

home = Path.home()
osu_path = str(home) + r"\AppData\Local\osulazer\current\osu!.exe"
osu_installer_path = str(home) + r"\install.exe"

osu_installer_url = 'https://github.com/ppy/osu/releases/latest/download/install.exe'

def ensureOsu() -> None:
    if os.path.isfile(osu_path):
        return
    if not os.path.isfile(osu_installer_path):
        urllib.request.urlretrieve(osu_installer_url, 'install.exe')
        os.replace('install.exe', osu_installer_path)
    os.system(osu_installer_path)

while True:
    if not ('osu!.exe' in (p.name() for p in psutil.process_iter())):
        ensureOsu()
        os.system(osu_path)
