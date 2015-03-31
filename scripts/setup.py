#!/usr/local/bin/python3

#
# Create an exe using cx_Freeze
#
# Instructions:
# pip install cx_freeze
# cd scripts
# python setup.py build
#

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'packages': ['os', 'github3', 'subprocess', 'shutil'], 'excludes': []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'pull',
    version = '0.1',
    description = 'Pull students work repos!',
    options = {'build_exe': build_exe_options},
    executables = [Executable(
        '../pull.py',
        icon = 'resources/icon.ico',
        base=base
        )]
)
