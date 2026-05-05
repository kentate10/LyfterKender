#Lyfter

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)


r1Wid= int(input("Enter width of rectangle 1: "))
r1Hei = int(input("Enter height of rectangle 1: "))

r1 = Rectangle(r1Wid, r1Hei)


print(r1.get_area())
print(r1.get_perimeter())

