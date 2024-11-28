class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"
    
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"
    
class FormulaOneCar(Car):
    def __init__(self, brand, model, color, top_speed, team):
        super().__init__(brand, model, color)
        self.top_speed = top_speed
        self.team = team

    def __str__(self):
        return f"{self.color} {self.brand} {self.model} {self.team} with a top speed of {self.top_speed} km/h"

class Helicopter(Vehicle):
    def __init__(self, brand, model, color, max_altitude):
        super().__init__(brand, model)
        self.color = color
        self.max_altitude = max_altitude

    def __str__(self):
        return f"{self.color} {self.brand} {self.model} with a max altitude of {self.max_altitude} meters"
    
def main():
    car = Car("Audi", "A4", "Black")
    print(car.__class__.__name__ + ": " + str(car))
    
    f1_car = FormulaOneCar("Ferrari", "SF1000", "Red", 375, "Scuderia Ferrari")
    print(f1_car.__class__.__name__ + ": " + str(f1_car))
    
    helicopter = Helicopter("Airbus", "H145", "White", 5000)
    print(helicopter.__class__.__name__ + ": " + str(helicopter))

if __name__ == "__main__":
    main()