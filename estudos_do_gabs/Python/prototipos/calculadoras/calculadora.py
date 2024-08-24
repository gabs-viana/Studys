num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
tipo_de_operacao = input("Escolha o tipo de operação (+,-,/,*): ")
if tipo_de_operacao == "+":
    print(num1 + num2)
elif tipo_de_operacao == "-":
    print(num1 - num2)
elif tipo_de_operacao == "/":
    print(num1 / num2)
elif tipo_de_operacao == "*":
    print(num1 * num2)
else:
    print("Sua resposta não condiz com nenhuma de nossas operações.")