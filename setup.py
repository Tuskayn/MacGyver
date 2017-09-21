import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame"],
                     "include_files": ["img", "maps", "sounds", "constant.py", "classy.py"],
                     "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="macgyver.py",
      version="0.1",
      description="MacGyver game",
      options={"build_exe": build_exe_options},
      executables=[Executable("macgyver.py", base=base)])
