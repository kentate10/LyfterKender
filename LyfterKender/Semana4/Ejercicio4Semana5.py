# Cree un programa que elimine todos los números impares de una lista.

my_list = [3, 17, 22, 4, 5, 6, 9, 100, 55, 78, 13]
for i in my_list[:]:
    if i % 2 != 0:
        my_list.remove(i)
print(my_list)