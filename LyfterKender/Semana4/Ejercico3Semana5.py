# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.


my_list = [4, 3, 6, 1, 7]

# Intercambia el primer que es representado por 0 y último elemento ques -1
my_list[0], my_list[-1] = my_list[-1], my_list[0]

#funnciona en cualquier lista pero da error si es una lista vacia


print(my_list)