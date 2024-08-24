num1 = int(input("Informe o 1° número: "))
num2 = int(input("Informe o 2° número: "))

# Criando uma instância da calculadora

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
       return self.num1 + self.num2
    
    def subt(self):
        return self.num1 - self.num2
    
    def mult(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

calc = Calculadora(num1, num2)

resultado = calc.soma()
resultado2 = calc.subt()
resultado3 = calc.mult()
resultado4 = calc.div()
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)