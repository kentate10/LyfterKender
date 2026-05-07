#4Pilares
class BankAccount():
    def __init__(self, balance):
        self.balance = balance
        return balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class SaveAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)  #llama al constructor del padre con super
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        
        if (self.balance - amount) < self.min_balance:
            raise ValueError(f"No se puede retirar ${amount}. El balance queda en ${self.balance - amount}, por debajo del min permitido de ${self.min_balance}")
        
       
        super().withdraw(amount)




# ============================================
# HERENCIA CON CLASES ABSTRACTAS
# ============================================
from abc import ABC, abstractmethod
import math

# Clase abstracta Shape
class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass


# Clase Circle hereda de Shape
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


# Clase Square hereda de Shape
class Square(Shape):
    
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side


# Clase Rectangle hereda de Shape
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# ============================================

# Clase que puede volar
class Flyable:
    def fly(self):
        return "Puedo volar"

# Clase que puede nadar
class Swimmable:
    def swim(self):
        return "Puedo nadar"

# Pato hereda de ambas clases (herencia múltiple)
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return "Quack!"


# ============================================


if __name__ == "__main__":
    print("=" * 50)
    print("EJEMPLO ")
    print("=" * 50)
    

    # Crear un pato
    duck = Duck("Donald")
    print(f"\n{duck.name} dice: {duck.quack()}")
    print(f"{duck.name}: {duck.fly()}")
    print(f"{duck.name}: {duck.swim()}")
