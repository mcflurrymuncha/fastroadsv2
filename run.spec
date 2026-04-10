# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['webview.platforms.edgechromium', 'webview.platforms.mshtml', 'webview.platforms.winforms', 'webview.platforms.cef']
hiddenimports += collect_submodules('webview')


a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[('index.html', '.'), ('manifest.json', '.'), ('favicon_circle.svg', '.'), ('alea.min.js', '.'), ('null.html', '.'), ('static', 'static'), ('favicon_circle.ico', '.')],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\louie\\Downloads\\fastroads-master\\fastroads-master\\favicon_circle.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
)
