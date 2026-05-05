import csv
import os

# esto exporta los datos actuales a un archivo CSV
def export_data(student_list):
    filename = "estudiantes.csv"  # definido localmente
    # abro el archivo en modo escritura, con encoding para que no se bugueen los acentos
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # escribo los headers del archivo
        writer.writerow(["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias"])

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

# esto importa datos desde un CSV si ya fue exportado antes
def import_data(student_list):
    filename = "estudiantes.csv"  # definido localmente
    # primero reviso si el archivo existe, si no, le aviso al usuario
    if not os.path.exists(filename):
        print("No se encontró un archivo previamente exportado.")
        return

    # si el archivo sí existe, lo abro para leerlo
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # limpio la lista actual por si ya tenía datos
        student_list.clear()

        # recorro cada fila del archivo y convierto la info en diccionarios
        for row in reader:
            student = {
                "name": row["Nombre"],
                "section": row["Sección"],
                "grades": {
                    "español": float(row["Español"]),
                    "inglés": float(row["Inglés"]),
                    "sociales": float(row["Sociales"]),
                    "ciencias": float(row["Ciencias"])
                }
            }
            # agrego cada estudiante a la lista
            student_list.append(student)

    print("Datos importados exitosamente.")
