

num = int(input("Digite o número desejado inicial: "))
porc = int(input("Digite a porcentagem requisitada deste número: "))
porc_math = porc / 100
result = num * porc_math

print(f"{porc}% de {num} equivale a {result:.2f}")
