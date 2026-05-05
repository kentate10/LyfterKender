#Dado el nombre y apellido de un empleado, y el dominio .com de una empresa, genere su email usando el formato <nombre>.#

Nombres_Empleado = input('Digite el nombre del empleado: ')
Apellido_Empleado = input('Digite el apellido del empleado: ')
Dominio_Empresa = input('Ingrese el dominio del correo de empresa: ')

Correo_Generado = Nombres_Empleado + '.' + Apellido_Empleado +'@'+ Dominio_Empresa + '.com' 

print('El Correo del empleado con los previos datos brindados es: ', Correo_Generado)