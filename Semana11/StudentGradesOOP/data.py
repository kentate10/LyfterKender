import csv
import os
import students



# Este modulo maneja la exportación e importación de datos de estudiantes a un archivo CSV, tiene la funcion de conversion de  datos a diccionario
FILENAME = "estudiantes.csv"

#______________CODIGO COMENTADO VIEJO ____________________
# esto exporta los datos actuales a un archivo CSV
# def export_data(student_list):
#     # abro el archivo en modo escritura, con encoding para que no se bugueen los acentos
#     with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)

#         # escribo los headers del archivo
#         writer.writerow(["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias"])

#         # ahora voy escribiendo los datos de cada estudiante
#         for student in student_list:
#             grades = student['grades']
#             writer.writerow([
#                 student['name'],
#                 student['section'],
#                 grades["español"],
#                 grades["inglés"],
#                 grades["sociales"],
#                 grades["ciencias"]
#             ])

#     print("Datos exportados exitosamente.")

# esto importa datos desde un CSV si ya fue exportado antes

def export_data(student_list):
    # abro el archivo en modo escritura, con encoding para que no se bugueen los acentos
   def export_data(student_list):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias"]
        writer = csv.DictWriter(file, fieldnames=fieldnames) 

        writer.writeheader()#escribo los headers del archivo
        
        for student in student_list:
            writer.writerow(student.to_dict())

    print("Datos exportados exitosamente.")

        # ahora voy escribiendo los datos de cada estudiante
        for student in student_list:
            grades = student['grades']
            writer.writerow([
                student['name'],
                student['section'],
                grades["español"],
                grades["inglés"],
                grades["sociales"],
                grades["ciencias"]
            ])

    print("Datos exportados exitosamente.")

#esto importa datos desde un CSV si ya fue exportado antes


def import_data(student_list):
    if not os.path.exists(FILENAME):
        print("No se encontró un archivo previamente exportado.")
        return

    with open(FILENAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file) #diccionario para leer el CSV, dicreader es un objeto que permite leer el CSV como un diccionario
        student_list.clear() # se usa para borrar dastos previos en la lista de estudiantes y no duplicarlos

        for row in reader:
            grades = {
                "español": float(row["Español"]),
                "inglés": float(row["Inglés"]),
                "sociales": float(row["Sociales"]),
                "ciencias": float(row["Ciencias"])
            }
            student = Student(row["Nombre"], row["Sección"], grades)
            student_list.append(student)

    print("Datos importados exitosamente.")

|#recordatorio
##el dicionario anterior seria algo asi de ejemplo:
# student = Student("Ana", "7A", {
#     "español": 85.0,
#     "inglés": 90.0,
#     "sociales": 88.0,
#     "ciencias": 92.0
# })
