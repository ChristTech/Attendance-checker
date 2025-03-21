# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
from kivy_deps import sdl2
from kivy_deps import glew  # required for Windows adjust as needed for other OS
from kivymd import hooks_path as kivymd_hooks_path
from kivymd.icon_definitions import md_icons
import encodings

# Manually specify the paths to the SDL2 and GLEW binaries
sdl2_bin_path = os.path.join(os.path.dirname(sdl2.__file__), 'bin', 'sdl2.dll')
glew_bin_path = os.path.join(os.path.dirname(glew.__file__), 'bin', 'glew32.dll')
encodings_path = os.path.dirname(encodings.__file__)  # Get encodings path


binaries = [
    (sdl2_bin_path, '.'),  # Copy sdl2.dll to the root of the dist folder
    (glew_bin_path, '.'),  # Copy glew.dll to the root of the dist folder
]

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[(encodings_path, 'encodings')], 
    hiddenimports=[
        'kivymd',              # ensure KivyMD is included
        'pandas',              # include pandas if not automatically detected
        'kivy_deps.sdl2',      # extra dependencies for Kivy (Windows)
        'kivy-deps.glew',
        'encodings',
        'codecs',
        'kivymd.icon_definitions.md_icons',
        'encodings.utf_8',  # Ensure UTF-8 encoding support
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=False,
    name='TARMCompare',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TARMCompare',
)
