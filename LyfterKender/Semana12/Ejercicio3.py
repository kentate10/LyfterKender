class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity  # capacidad en kWh
    
    def charge(self):
        print(f"Cargando batería de {self.battery_capacity} kWh...")

class GasolineCar:
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity  # capacidad en litros

    def refuel(self):
        print(f"Llenando tanque de {self.fuel_capacity} litros...")
