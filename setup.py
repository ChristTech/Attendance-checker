import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["pandas", "kivy", "kivymd", "os", "kivy_deps.sdl2"], 'excludes': ['tkinter']}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'TARM Attendance Comparator', icon='icon.png')
]

setup(name='TARM Attendance Comparator',
      version = '0.1',
      description = 'AN attendance comparing application for TARM Ilorin by CHRISTTech',
      options = {'build_exe': build_options},
      executables = executables)
