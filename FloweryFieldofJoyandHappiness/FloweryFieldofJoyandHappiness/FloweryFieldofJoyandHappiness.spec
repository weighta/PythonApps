# -*- mode: python -*-

block_cipher = None


a = Analysis(['FloweryFieldofJoyandHappiness.py'],
             pathex=['C:\\Users\\Alex Weight\\Documents\\Visual Studio 2015\\Projects\\FloweryFieldofJoyandHappiness\\FloweryFieldofJoyandHappiness'],
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
          name='FloweryFieldofJoyandHappiness',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
