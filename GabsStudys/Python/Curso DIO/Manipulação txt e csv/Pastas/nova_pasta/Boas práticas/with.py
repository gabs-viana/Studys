from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "novo_arquivo.txt", "r") as arquivo:
        print(arquivo.read())
except IOError:
    print(f"Erro ao abrir o arquivo. {exc}")


# try:
#     with open(ROOT_PATH / "arquivo_utf8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos usando Python")
# except IOError:
#     print(f"Erro ao abrir o arquivo. {exc}")

try:
    with open(ROOT_PATH / "arquivo_utf8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo. {exc}")