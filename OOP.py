# Base class: Superhero
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self._power = power       # Encapsulated attribute
        self.level = level

    def display_info(self):
        print(f" Name: {self.name}, Power: {self._power}, Level: {self.level}")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self._power}!")

# Subclass: StrongHero
class StrongHero(Superhero):
    def use_power(self):
        print(f"{self.name} smashes with incredible strength using {self._power}!")




##Polymorphism with Vehicles
# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        print(" Car is driving...")

class Plane(Vehicle):
    def move(self):
        print(" Plane is flying...")

class Boat(Vehicle):
    def move(self):
        print(" Boat is sailing...")
