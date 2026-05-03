class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")


class Car(Vehicle):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}")
        print("-" * 30)


class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.bike_type}")
        print("-" * 30)


class Truck(Vehicle):
    def __init__(self, brand, speed, load_capacity):
        super().__init__(brand, speed)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Load Capacity: {self.load_capacity} tons")
        print("-" * 30)


vehicles = []

while True:
    print("\n1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\n1. Car\n2. Bike\n3. Truck")
        v_type = input("Select vehicle type: ")

        brand = input("Enter brand: ")
        speed = int(input("Enter speed: "))

        if v_type == "1":
            seats = int(input("Enter seats: "))
            v = Car(brand, speed, seats)

        elif v_type == "2":
            bike_type = input("Enter bike type: ")
            v = Bike(brand, speed, bike_type)

        elif v_type == "3":
            load = int(input("Enter load capacity: "))
            v = Truck(brand, speed, load)

        else:
            print("Invalid type")
            continue

        vehicles.append(v)
        print("Vehicle added successfully")

    elif choice == "2":
        if not vehicles:
            print("No vehicles found")
        else:
            for v in vehicles:
                v.display_info()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")