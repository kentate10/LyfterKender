
def decorator_Return(func):
    def wrapper(*args, **kwargs):
        print("Aca entra el decorador")
        result = func(*args, **kwargs) #se ejecuta la funcion original, la que vamos a decorar 
        print(f"Los datos son: {result}")
        print("Aca sale el decorador")
        # se retorna el resultado de la funcion original
        return result
    return wrapper

@decorator_Return # se decora la funcion test_decorator
def test_decorator():
    
    personas = input("introduzca los nombres separados por comas: ")
    personas = [persona.strip() for persona in personas.split(",")]

    pelo= input("introduzca el color del pelo: ")
    ojos = input("introduzca el color de los ojos: ")
    altura = input("introduzca la altura: ")

    return personas, {
        "pelo": pelo,
        "ojos": ojos,
        "altura": altura
    }

test_decorator() # se ejecuta la funcion decorada
