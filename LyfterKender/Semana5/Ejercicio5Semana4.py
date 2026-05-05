# #5. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70). 
#     2. Cuantas notas tiene desaprobadas (menor a 70).  
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.

print('Programa para resumir notas de estudiantes')

i=0
notas = []
notas_aprobadas = []
notas_desaprobadas = []
ciclo = True 
while ciclo:
    notas.append(int(input("Ingrese las notas de su esudiante: ")))
    stop = input("Desea ingresa otra nota? si/no ")
    if stop != 'si':
         ciclo = False
for x in notas:
    if x  >= 70:
        notas_aprobadas.append(x)
    else:
        notas_desaprobadas.append(x)

#     1. Cuantas notas tiene aprobadas (mayor a 70). 
#     2. Cuantas notas tiene desaprobadas (menor a 70).          
print('notas aprobadas: ', notas_aprobadas,' notas repobradas: ',notas_desaprobadas)
print(f"tiene un total de {len(notas_aprobadas)} notas aprobadas y {len(notas_desaprobadas)} notas desaprobadas")        
#-----------------------------------------------------#

#promedio de notas        
suma_total = sum(notas)
prom_general= suma_total / len(notas)
print(f"Su promedio general de notas es de {prom_general}")
#-----------------------------------------------------#

#     4. El promedio de las aprobadas.
suma_aprobada = sum(notas_aprobadas)
prom_aprobadas = suma_aprobada / len(notas_aprobadas) if notas_aprobadas else 0 #se usa la condicion para evitar el error que tuve porque intento' dividir entre 0
print(f'promedio de notas aprobadas {[prom_aprobadas]}')
#-----------------------------------------------------#

#     5. El promedio de las desaprobadas.
suma_desaprobadas = sum(notas_desaprobadas)
prom_desaprobadas = suma_desaprobadas / len(notas_desaprobadas) if notas_desaprobadas else 0
print(f'promedio de notas desaprobadas {prom_desaprobadas}')