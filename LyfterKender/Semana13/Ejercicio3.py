from datetime import datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    
    @property
    def age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
def adult_check(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("Se esperaba una instancia de User")
        if user.age < 18:
            raise PermissionError("El usuario no es mayor de edad")
        return func(user, *args, **kwargs)
    return wrapper

# Ejemplo decorada

@adult_check
def ver_pelicula_adulta(user):
    return print("Puedes ver la película.")               

kender = User("2013-05-15")  # usuario menor de edad

ver_pelicula_adulta(kender)