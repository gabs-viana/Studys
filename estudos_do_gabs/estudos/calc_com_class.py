num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
       return self.num1 + self.num2

calc = Calculadora(num1, num2)

resultado = calc.soma()
print(resultado)