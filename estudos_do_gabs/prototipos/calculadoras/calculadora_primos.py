num = int(input("Digite o número inicial: "))

if num % 2 == 0:
    print(f"{num} não é primo!")
elif num % 3 == 0:
    print(f"{num} não é primo!")
elif num % 5 == 0:
    print(f"{num} não é primo!")
elif num % 7 == 0:
    print(f"{num} não é primo!")
elif num % 13 == 0:
    print(f"{num} não é primo!")
else:
    print(f"{num} é um número primo!")