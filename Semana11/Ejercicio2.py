#EJERCICIO2


class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
    
    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus.")
        else:
            print("The bus is full. Cannot add more passengers.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has left the bus.")
        else:
            print(f"{person.name} is not on the bus.")

