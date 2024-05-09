import os
import subprocess

from pyqadmin import admin 

@admin 
def test():
    print("У меня права администратора:)")
    subprocess.run(['powershell.exe','wininit'])
test()