

def verificar_palindromo(palavra):
    palavras_nospace = palavra.replace(" ", "")
    palavra_invertida = "".join(reversed(palavras_nospace))
    if palavra_invertida == palavras_nospace:
        return True
    else:
        return False
    
print(verificar_palindromo("ovo"))
print(verificar_palindromo("radar"))
print(verificar_palindromo("python"))
print(verificar_palindromo("Flamengo"))
print(verificar_palindromo("ame o poema"))