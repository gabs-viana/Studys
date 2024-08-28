class Carro:
    def __init__(self,marca, cor, modelo, ano):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
    
    def ligar_motor(self):
        print(f"{self.marca} {self.modelo} está ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join
        ([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Chevrolet(Carro):
    def alarme_apitando(self):
        print("pi pi pi pi pi pi pi")

class Peugeot(Carro):
    pass

class Wolksvagen(Carro):
    pass

carro1 = Chevrolet("Chevrolet", "Prata", "Celta", "2006")
carro1.ligar_motor()
carro1.alarme_apitando()

carro2 = Peugeot("Peugeot", "Azul", "208", "2024")
carro2.ligar_motor()

carro3 = Wolksvagen("Wolksvagen", "Preto", "Jetta", "2018")
carro3.ligar_motor()
print(carro1)