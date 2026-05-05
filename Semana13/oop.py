#Lyfter

#Area de Rectangulo


# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         
#     def get_area(self):
#         return self.width * self.height
#     
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
# 
# 
# r1Wid= int(input("Enter width of rectangle 1: "))
# r1Hei = int(input("Enter height of rectangle 1: "))
# 
# r1 = Rectangle(r1Wid, r1Hei)
# 
# 
# print(r1.get_area())
# print(r1.get_perimeter())

#-----------------Segundo Codigo--------------------------#

# class Pet ():
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#     def show(self):
#         print(f"{self.name} is a {self.kind}")

# class Dog(Pet):
#     def speak(self):
#         print("Woof!")

# class Cat(Pet):
#     def speak(self):
#         print("Meow!")
        
# d1= Dog("Chubby", "dog")
# d1.show()
# d1.speak()

# c1 = Cat("Tom", "cat")
# c1.show()
# c1.speak()

#--------------------Tercer Codigo---------------------


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        print(f"{self.name} - ${self.price} x {self.quantity} unidades")

    def get_total_price(self):
        return self.price * self.quantity


class Inventory():
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Producto '{product.name}' agregado")
    
    def show_all_products(self):
        print("\n=== INVENTARIO ===")
        if len(self.products) == 0:
            print("Inventario vacío")
        else:
            for product in self.products:
                product.show()
    
    def calculate_total_value(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total


inventory = Inventory()

p1 = Product("Laptop", 800, 5)
p2 = Product("Mouse", 20, 15)
p3 = Product("Teclado", 50, 10)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

inventory.show_all_products()

print(f"\nValor total: ${inventory.calculate_total_value()}")