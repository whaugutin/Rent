class Vehicle():
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nDaily Rate: $ {self.daily_rate} US")
        

class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_seat):
        super().__init__(make, model, year, daily_rate)
        self.num_seat = num_seat

    def display_info(self):
        super().display_info()
        print(f"Number of Seats: {self.num_seat}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, engine_type):
        super().__init__(make, model, year, daily_rate)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"The engine's type: {self.engine_type}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, frame_type):
        super().__init__(make, model, year, daily_rate)
        self.frame_type = frame_type

    def display_info(self):
        super().display_info()
        print(f"The frame's type: {self.frame_type}")
    
class Rental():
    def __init__(self, vehicule, rental_days):
        self.vehicule = vehicule
        self.rental_days = rental_days

    def calculate_total_cost(self):
        return round(self.vehicule.daily_rate * self.rental_days, 2)
    
    def display_receipt(self):
        print("==========Fich==========")
        self.vehicule.display_info()
        print(f"Rentals Days: {self.rental_days}")
        print(f"Total cost: $ {self.calculate_total_cost()} US")


# Test
car = Car("Toyota", "Supra", 2023, 200, 2)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 69.99, "V-twin")
bicycle = Bicycle("Trek", "FX", 2023, 20, "Hybrid")

print()
car.display_info()
print()
motorcycle.display_info()
print()
bicycle.display_info()
print()
rental_car = Rental(car, 3)
rental_car.display_receipt()
print()
rental_motorcycle = Rental(motorcycle, 2)
rental_motorcycle.display_receipt()
print()
rental_bicycle = Rental(bicycle, 20)
rental_bicycle.display_receipt()
print()