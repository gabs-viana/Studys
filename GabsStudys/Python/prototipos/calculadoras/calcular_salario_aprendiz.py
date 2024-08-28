# Código para imprimir o quanto receberei de acordo com meu salário

def salario_liquido():
    salario_bruto = float(input("Informe seu sálario bruto: "))
    impostos = 0.06812 * 1000
    salario_liquido = salario_bruto - impostos
    return salario_liquido

salario = salario_liquido()
print(f"O seu salário descontado todos os impostos é de R${salario:.2f}")

