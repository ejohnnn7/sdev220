'''
Student Name: Elizabeth John
File Name: vehicleApp.py
Description:
The purpose of this app is to collect car details from the user using vehicle classes, and prints the results in a readable format.
'''

# Vehicle Super Class
# This class represents a general vehicle.
# It stores the type of vehicle (car, truck, etc.) and its color.
class Vehicle:
    def __init__(self, vehicle_type):
        # Attribute to store the type of vehicle
        self.vehicle_type = vehicle_type

# Automobile Subclass
# this class inherits from Vehicle and adds car-specific attributes.
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # call the parent class constructor
        super().__init__(vehicle_type)
        
        # stores the automobile details
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Helper function: doors input
# ensures the user enters either 2 or 4 doors.
def get_doors():
    while True:
        try:
            doors = int(input("Enter the number of doors (2 or 4): "))
            if doors in [2, 4]:
                return doors
            else:
                print("Invalid input. Please enter either 2 or 4.")
        except ValueError:
            print("Invalid input. Please enter a numeric value (2 or 4).")

# Helper function: roof input
# ensures the user enters either 'solid' or 'sunroof'.
def get_roof():
    while True:
        roof = input("Enter the type of roof (solid or sunroof): ").strip().lower()
        if roof in ['solid', 'sunroof']:
            return roof
        else:
            print("Invalid input. Please enter either 'solid' or 'sunroof'.")

# Main Program Function
def main():
    # vehicle type is always "car" per assignment instructions
    vehicle_type = "car"

    # collect user input for car details
    year = input("Enter the car's year: ")
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")
    doors = get_doors()
    roof = get_roof()

    # create an automobile object with the user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # display vehicle information
    print("\nVehicle Information:")
    print(f"Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of Doors: {car.doors}")
    print(f"Type of Roof: {car.roof}")

# Run the main program
if __name__ == "__main__":
    main()