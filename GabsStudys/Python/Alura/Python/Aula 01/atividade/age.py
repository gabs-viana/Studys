numero = int(input("Insira um número: "))

match numero:
    case _ if numero % 2 == 0:
        print("Número par")
    case _ if numero % 2 != 0:
        print("Número ímpar")

idade = int(input("Insira sua idade: "))
match idade:
    case _ if idade > 0 and idade < 12:
        print("Criança")
    case _ if idade >= 13 and idade < 18:
        print("Adolescente")
    case _ if idade >= 18:
        print("Adulto")

nome_esperado = "Gabs"
senha_esperada = "1234"
nome = input("Insira seu nome: ")
senha = int(input("Insira sua senha: "))
match (nome, senha):
    case (nome_esperado, senha_esperada):
        print("Bem-vindo, Gabs!")
    case _:
        print("Usuário ou senha inválidos")

coords_x = int(input("Insira a coordenada x: "))
coords_y = int(input("Insira a coordenada y: "))
match (coords_x, coords_y):
    case _ if coords_x and coords_y > 0:
        print("Primeiro quadrante")
    case _ if coords_x < 0 and coords_y > 0:
        print("Segundo quadrante")
    case _ if coords_x < 0 and coords_y < 0:
        print("Terceiro quadrante")
    case _ if coords_x > 0 and coords_y < 0:
        print("Quarto quadrante")
    case _:
        print("Origem ou eixo")