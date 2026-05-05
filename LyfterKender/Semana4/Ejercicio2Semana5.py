#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "pizza con pina"

for i in reversed(range(len(my_string))):
    print(my_string[i])