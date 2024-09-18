import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent


# os.mkdir(ROOT_PATH / "nova_pasta")

# arquivo = open(ROOT_PATH / "novo_arquivo.txt", "w")
# arquivo.close()

# os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "alterado.txt")

# os.remove(ROOT_PATH / "novo_arquivo.txt")

shutil.move(ROOT_PATH / 'alterado.txt', ROOT_PATH / "nova_pasta" / "alterado.txt")