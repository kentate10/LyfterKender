#ejercicio5 

def contar_mayus_minus(oracion):
    mayusculas = 0
    minusculas = 0
    for letra in oracion:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1
    return mayusculas, minusculas


oracion = "Hola Esto Es UnA PrUeBa"
mayus, minus = contar_mayus_minus(oracion)
print(f"Mayusculas: {mayus}, Minusculas: {minus}")
