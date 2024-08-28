
def contar_letrinhas(palavra):
    contador_vogais = 0
    contador_consoantes = 0
    vogais = "aeiou"

    for letra in palavra:
        if letra.lower() in vogais:
            contador_vogais += 1
        else:
            contador_consoantes += 1

        resposta = f"""
Palvra: {palavra}        
Número de vogais: {contador_vogais}
Número de consoantes: {contador_consoantes}
"""
        
    return resposta

print(contar_letrinhas("python"))
print(contar_letrinhas("flamengo"))
print(contar_letrinhas("paralelepipedo"))