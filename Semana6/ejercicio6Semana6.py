
def ordenar_palabras(cadena):
    
    # Dividir
    
    lista_palabras = cadena.split('-')
    # Sorted para ordenar alfabeticamente 
    lista_ordenada = sorted(lista_palabras)
    # Join para volver a unir la lista con el guion 
    return '-'.join(lista_ordenada)


cadena = "python-variable-funcion-computadora-monitor"

resultado = ordenar_palabras(cadena)

print(resultado)  
