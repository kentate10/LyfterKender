
#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

nombre_USR = input("Ingrese su nombre: ")
apellido_USR = input("Ingrese su apellido: ")
edad_USR = int(input("Ingrese su edad: "))


if edad <= 2:
    categoria = "bebé"
elif edad <= 11:
    categoria = "niño"
elif edad <= 12:
    categoria = "preadolescente"
elif edad <= 17:
    categoria = "adolescente"
elif edad <= 25:
    categoria = "adulto joven"
elif edad <= 59:
    categoria = "adulto"
else:
    categoria = "adulto mayor"


print(f"{nombre_USR} {apellido_USR}, con {edad_USR} años, eres {categoria}.")