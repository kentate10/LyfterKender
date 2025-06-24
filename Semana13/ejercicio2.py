def Deco_check (func):
    def wrapper(*args, **kwargs):
        print("aca entra el decorador para validar los datos")

        for check in list(args) + list((kwargs).values()):
           if not isinstance(check, (int, float)):
                raise TypeError(f"El dato {check} no es un numero") #se usa raise para detener lo que se corre y tire el error 
        #aca abajo ya se ejcutaria la funcinon si todo el valido 
 
        result = func(*args, **kwargs) 
             
        return result
    return wrapper
