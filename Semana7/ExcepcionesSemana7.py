##se investiga sobre las excepciones por aparte para poder hacer el programa sin problemas siguiendo la idea,


def calculadora():
    numero_actual = 0

    while True:
        try:
            print(f"""
============================
    Calculadora de Línea 
============================
Número Actual: {numero_actual}

Selecciona una operación:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
6. Salir
============================
            """)

            opcion = input("Ingresa tu opción (1-6): ")

            # Validar opcion
            if opcion not in ['1', '2', '3', '4', '5', '6']:
                raise ValueError("Opción inválida. Selecciona una opción válida del 1 al 6.")

            # Opción para salir
            if opcion == '6':
                print("\nSaliendo de la calculadora. ¡Adiós!")
                break

            # Si la opción es borrar resultado, no se solicita un número
            if opcion == '5':
                numero_actual = 0
                print("Resultado borrado. Número actual restablecido a 0.")
                continue

            # Solicitar el número
            try:
                nuevo_numero = float(input("Ingresa un número: "))
            except ValueError:
                raise ValueError("Número inválido. Por favor, ingresa un número válido.")

            # Realizar la operación correspondiente
            if opcion == '1':  # Suma
                numero_actual += nuevo_numero
            elif opcion == '2':  # Resta
                numero_actual -= nuevo_numero
            elif opcion == '3':  # Multiplicación
                numero_actual *= nuevo_numero
            elif opcion == '4':  # División
                if nuevo_numero == 0:
                    raise ZeroDivisionError("Error: No se puede dividir entre cero.")
                numero_actual /= nuevo_numero

        except ValueError as ve:
            print(f"\nError: {ve}")
        except ZeroDivisionError as zde:
            print(f"\n{zde}")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    calculadora()
