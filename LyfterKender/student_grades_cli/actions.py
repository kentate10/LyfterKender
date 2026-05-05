# Esta función es para agregar un nuevo estudiante a la lista
def add_student(student_list):
    name = input("Nombre completo: ")
    section = input("Sección (ej. 11B): ")
    grades = {}

    # Aquí pido las 4 materias, una por una
    for subject in ["Español", "Inglés", "Sociales", "Ciencias"]:
        while True:
            try:
                # Pido la nota y reviso que sea un número entre 0 y 100
                grade = float(input(f"Nota de {subject}: "))
                if 0 <= grade <= 100:
                    grades[subject.lower()] = grade  # lo guardo con el nombre en minúscula
                    break
                else:
                    print("❌ La nota debe estar entre 0 y 100.")
            except ValueError:
                print("❌ Ingrese un número válido.")

    # Guardo todo lo del estudiante en un diccionario
    student = {
        "name": name,
        "section": section,
        "grades": grades
    }

    # y lo agrego a la lista
    student_list.append(student)
    print("✅ Estudiante agregado con éxito.")

# Esta muestra a todos los estudiantes que ya agregué
def view_students(student_list):
    if not student_list:
        print("No hay estudiantes registrados.")
        return

    for indx, student in enumerate(student_list, start=1):
        print(f"{indx}. {student['name']} ({student['section']}) - Notas: {student['grades']}")

# Aquí muestro el top 3 de estudiantes con mejor promedio
def view_top_students(student_list):
    if len(student_list) < 1:
        print("No hay suficientes estudiantes.")
        return

    # Ordeno los estudiantes por su promedio de notas, de mayor a menor
    sorted_students = sorted(
        student_list,
        key=lambda s: sum(s['grades'].values()) / len(s['grades']), #lambda es una funciona sobre una sola linea, el s extrae los datos
        reverse=True
    )[:3]

    print(" Top 3 estudiantes:")
    for student in sorted_students:
        avg = sum(student['grades'].values()) / len(student['grades'])
        print(f"{student['name']} ({student['section']}) - Promedio: {avg:.2f}")

# Esto es para ver el promedio general de todos los estudiantes (el promedio de sus promedios)
def view_general_average(student_list):
    if not student_list:
        print("No hay estudiantes registrados.")
        return

    # Saco el promedio de cada estudiante, y luego saco el promedio de todos esos
    total_avg = sum(
        sum(s['grades'].values()) / len(s['grades']) for s in student_list
    ) / len(student_list)

    print(f" Promedio general de todos los estudiantes: {total_avg:.2f}")
