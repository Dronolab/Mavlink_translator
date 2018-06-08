# -*- mode: python -*-

block_cipher = None


a = Analysis(['Dronolab_mavlink_translator.py'],
             pathex=['C:\\Users\\Potvi\\PycharmProjects\\Dronolab_mavlink_translator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Dronolab_mavlink_translator',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='logo-final.ico')
