class Carro:
    def __init__(self, cor, marca, modelo, ano, valor):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Fon fon!")
        
    def parar(self):
        print(f"Parando o {self.modelo}")

    def correr(self):
        print("Vrummmmmm....")

#objetos       
carro1 = Carro("prata", "Chevrolet", "Celta", "2006", 10000)
carro2 = Carro("preto", "Fiat", "Palio", "2003", 9000)
carro3 = Carro("preto", "Chevrolet", "Impala", "1967", 67000)
carro4 = Carro("branco", "Toyota", "Prius", "2022", 90000)

#chamada de classes
carro1.parar()
carro2.parar()