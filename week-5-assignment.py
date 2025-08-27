# Base class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand                # Attribute: brand
        self.model = model                # Attribute: model
        self.battery_life = battery_life  # Attribute: battery life in hours

    def make_call(self, contact):
        if self.battery_life > 0:
            print(f"Calling {contact} from {self.brand} {self.model}... 📞")
            self.battery_life -= 1  # Simulate battery drain
        else:
            print("Battery is dead, please charge your phone!")

    def charge_battery(self, hours):
        self.battery_life += hours
        print(f"{self.brand} {self.model} is charged! Current battery life: {self.battery_life} hours.")

# Subclass representing a CameraPhone that extends Smartphone
class CameraPhone(Smartphone):
    def take_photo(self):
        if self.battery_life > 0:
            print(f"Taking a photo with {self.brand} {self.model}... 📸")
            self.battery_life -= 1  # Simulate battery drain
        else:
            print("Battery is dead, please charge your phone!")

# Creating an object of Smartphone
my_phone = Smartphone("Apple", "iPhone 13", 10)
my_phone.make_call("Alice")
my_phone.charge_battery(2)

# Creating an object of CameraPhone
my_camera_phone = CameraPhone("Samsung", "Galaxy S21", 8)
my_camera_phone.take_photo()
my_camera_phone.make_call("Bob")

# Base class for vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Car class that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Bicycle class that inherits from Vehicle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# List of vehicles
vehicles = [Car(), Plane(), Bicycle()]

# Demonstrating polymorphism
for vehicle in vehicles:
    vehicle.move()  # Calls the move method of each vehicle
