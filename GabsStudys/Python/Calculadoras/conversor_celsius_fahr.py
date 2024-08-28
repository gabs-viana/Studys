#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(self):
        self.fahrenheit = self.celsius * 1.8 + 32
        return self.fahrenheit

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = ConversorTemperatura(celsius)

fahrenheit = conversor.celsius_para_fahrenheit()
print(fahrenheit)