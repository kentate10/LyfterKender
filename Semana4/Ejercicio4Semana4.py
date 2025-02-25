#Cree un programa que le pida tres números al usuario y muestre el mayor.
print("Programa para ver cual numero es mayo, solo usar numeros enteros(: )")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero numero: "))
c = int(input("Ingrese el tercer numero numero: "))

if a > b and a> c:
    print(f"El numero mayor es {a}")
elif b > a and b > c:
    print(f"El numero mayor es {b}")
else:
    print(f"El numero mayor es {c}")