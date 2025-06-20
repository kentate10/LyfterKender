class Student:
    def __init__(self, name, section, grades):
        self.name = name
        self.section = section
        self.grades= grades 

        #este es un diccionario con las materias y sus notas
    
    def to_dict(self):
        return {
            "Nombre": self.name,
            "Sección": self.section,
            "Español": self.grades["español"],
            "Inglés": self.grades["inglés"],
            "Sociales": self.grades["sociales"],
            "Ciencias": self.grades["ciencias"]
        }