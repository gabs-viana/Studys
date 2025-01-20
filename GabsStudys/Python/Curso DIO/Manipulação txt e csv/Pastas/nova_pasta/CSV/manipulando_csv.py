import csv 
from pathlib import Path

ROOT_PATH = Path(__file__).parent
ID_COLUMN = 0
NAME_COLUMN = 1

#Criando um CSV
try:
    with open(ROOT_PATH / "usuarios.csv", "w", encoding="utf-8", newline="") as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerow(["Id", "Nome"])
       escritor.writerow(["1", "Gabs"])
       escritor.writerow(["2", "Felps"])
       escritor.writerow(["3", "Migs"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


#Leitor simples
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["Id"], row["Nome"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")