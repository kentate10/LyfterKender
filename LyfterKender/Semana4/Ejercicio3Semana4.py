import random 
#para poder buscar un numero random
num = [1,2,3,4,5,6,7,8,9,10]

secret_num = random.choice(num)

intentos = []

#print(secret_num)
#Comentado, se uso' para hacer pruebas


i = 0
while i == 0: 
    guess = int(input("Debes adivinar un numero random del 1 al 10 (:. Ingresa un numero para intentarlo: "))
    if guess == secret_num:
        i += 1
        print(f"Felicidades! el numero secreto era {secret_num}")
    else:
        intentos.append(guess)
        print(f"Intenta de nuevo!, tus previos intentos: {intentos} ")