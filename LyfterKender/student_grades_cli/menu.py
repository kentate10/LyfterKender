from actions import (
    add_student,
    view_students,
    view_top_students,
    view_general_average
)
from data import export_data, import_data

def show_menu(student_list):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Ver Top 3 estudiantes con mejor promedio")
        print("4. Ver nota promedio general")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Salir")

        choice = input("Seleccione una opción (1-7): ")
        if choice == "1":
            add_student(student_list)
        elif choice == "2":
            view_students(student_list)
        elif choice == "3":
            view_top_students(student_list)
        elif choice == "4":
            view_general_average(student_list)
        elif choice == "5":
            export_data(student_list)
        elif choice == "6":
            import_data(student_list)
        elif choice == "7":
            print("Gracias! GHasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
