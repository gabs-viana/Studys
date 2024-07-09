def quanto_fica():
    minutos = int(input("Quantos minutos o video tem? "))
    segundos = int(input("Quantos segundos o video tem? "))
    calculo1 = minutos / 1.5
    calculo2 = segundos / 1.5 + calculo1
    if calculo2 >= 60:
        calculo1 += 1
        calculo2 -= 60

    resultado = f"O tempo deste video em 1.5x é de {int(calculo1)}min e {int(calculo2)}s"
    return resultado

print(quanto_fica())