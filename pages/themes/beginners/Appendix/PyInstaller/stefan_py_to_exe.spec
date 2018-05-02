# -*- mode: python -*-

block_cipher = None


a = Analysis(['stefan_py_to_exe.py'],
             pathex=['/data/projects/www/wwwcourses.github.io/ProgressBG-VC-Python/pages/themes/beginners/Appendix/PyInstaller'],
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
          name='stefan_py_to_exe',
          debug=True,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
