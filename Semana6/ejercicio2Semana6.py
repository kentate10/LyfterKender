#ejercicio2Semana6

def scope():
    global numeros
    numeros = 3
    if numeros != 4:
        print('numero distinto')

scope()
print (numeros)