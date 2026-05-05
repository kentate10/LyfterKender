# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

def main():
    import json
    
    try:
        with open("pokemones.json", "r", encoding="utf-8") as file:
            pokemones = json.load(file)  # Intentamos leer el archivo
    except (FileNotFoundError, json.JSONDecodeError):
        pokemones = []  # Si el archivo no existe o está vacío, iniciamos con una lista vacía

    name = input('Nombre: ')
    typep = input('Tipo: ')
    level = int(input('Nivel: '))
    
    newPokemon = {
        'name': name,
        'type': typep,
        'level': level
    }
    pokemones.append(newPokemon)
    
    with open('pokemones.json', 'w', encoding="utf-8") as file:
        json.dump(pokemones, file, indent=4)
    print('Pokemon agregado')
    print("Pokemones: ", json.loads(open("pokemones.json", "r", encoding="utf-8").read()))

if __name__ == "__main__":
    main()
        