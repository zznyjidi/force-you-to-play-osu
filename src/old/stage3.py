import sys
import winreg
from pathlib import Path as b

p = f'"{sys.executable[0:-4]}w.exe"'
s = fr' "{b.home()}\start.py"'

k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(k, 'program', 0, winreg.REG_SZ, p+s)
winreg.CloseKey(k)
