numero = int(input("Digite o número a se localizar a raiz: "))
raiz_quadrada = numero ** 0.5
if raiz_quadrada.is_integer():
    print(f"A raiz quadrada de {numero} é {int(raiz_quadrada)}.")
else:
    print(f"A raiz quadrada de {numero} é {raiz_quadrada:.3f}.")