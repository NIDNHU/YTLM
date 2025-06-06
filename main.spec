from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files

# Collect compiled binaries for orjson and pydantic_core
binaries = collect_dynamic_libs('orjson') + collect_dynamic_libs('pydantic_core')

datas = collect_data_files('orjson') + collect_data_files('pydantic_core')

# Required files (manually added)
added_files = [
    ('src/icons/', 'icons'),
]

# Collect nicegui data files automatically (alternative)
datas = collect_data_files('nicegui')
datas += added_files

a = Analysis(
    ['src\\main.py'],
    pathex=['src'],
    binaries=binaries,
    datas=datas,
    hiddenimports=[
        'plyer.platforms.win.notification',
        'plyer.platforms.linux.notification',
        'plyer.platforms.darwin.notification',
        'orjson',
        'pydantic_core'
    ],
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
    a.binaries,
    a.datas,
    [],
    name='YTLM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='app.ico'
)
