from cx_Freeze import setup, Executable

setup(name='TelaLogin',
      version='1.0',
      description='descricao do programa',
      options={'build_exe': {'packages': ['sys', 'PyQt5']}},
      executables=[Executable(
          script='telaLogin.py',
          base=None
      )
      ]
      )
