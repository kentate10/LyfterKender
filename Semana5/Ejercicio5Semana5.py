
#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numeros = []
#lista donde guardaremos los numeros y ciclo en el que los pedimos y hacemos append

print("Ingrese 10 numeros:")
for i in range(10):
    numero = int(input(f"Numero {i + 1}: "))
    numeros.append(numero)
    
    numero_mayor = max(numeros)
    
print("Los numeros ingresados son:", numeros)
print("El numero mas alto de la lista es:", numero_mayor)