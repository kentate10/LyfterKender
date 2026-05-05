#para saber si un número es primo
def esPrimo(n):
    if n <= 1:
        return False
    for x in range(2, n):  
        if n % x == 0:  # si se encuentra un divisor, no es primo
            return False
    return True

# primos de una lista
def obtenerPrimos(lista):
    primos = [n for n in lista if esPrimo(n)]
    return primos


numeros = [1, 4, 6, 7, 13, 9, 67,33,56,78]
resultado = obtenerPrimos(numeros)
print(resultado)  
