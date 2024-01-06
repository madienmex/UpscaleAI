# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'tools.py', 'upscale.py'],
    pathex=[],
    binaries=[],
    datas=[('lib/tkinterdnd2/tkdnd/*', 'lib/tkdnd'), ('lib/tkinterdnd2/*', 'lib/tkinterdnd2')],
    hiddenimports=['tkinterdnd2', 'cv2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='UpscaleAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
