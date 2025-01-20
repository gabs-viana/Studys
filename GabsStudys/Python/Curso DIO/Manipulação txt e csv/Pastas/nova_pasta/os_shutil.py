import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / "nova_pasta1")

# arquivo = open(ROOT_PATH / "novo_arquivo.txt", "w")
# arquivo.close()
# arquivo = open(ROOT_PATH / "novo.txt", "w")
# os.rename(ROOT_PATH / "flamengo.txt", ROOT_PATH / "bah.txt")


shutil.move(ROOT_PATH / 'flamengo.txt', ROOT_PATH / "nova_pasta1" / "flamengo.txt")
