from cx_Freeze import setup, Executable

# Definindo o executável do seu jogo
executables = [Executable("main.py")]

# Configuração do cx_Freeze
setup(
    name="Pixel Runner",
    version="1.0",
    description="Jogo Pixel Runner",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["assets/"]}},
    executables=executables
)