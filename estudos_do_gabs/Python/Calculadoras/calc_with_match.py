def calculadora(op):
    def soma(a, b):
        return a + b
    def subt(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a / b
    
    match op:
        case "+":
            return soma
        case "-":
            return subt
        case "*":
            return mult
        case "/":
            return div
        
print(calculadora("+")(66, 66))
print(calculadora("-")(66, 66))
print(calculadora("*")(66, 66))
print(calculadora("/")(66, 66))