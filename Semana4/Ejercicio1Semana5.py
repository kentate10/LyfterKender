# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

#para revisar que sean del  mismo tamano
if len(first_list) == len(second_list):
    
    for i in range(len(first_list)):
        print(first_list[i], second_list[i])
        
#se usa el i para guardar la posicion en la que esta el elemento de lista que vamos a imnprimir