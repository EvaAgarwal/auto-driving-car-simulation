from simulation import Simulation

def main():
    print("Welcome to Auto Driving Car Simulation!\n")
    width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
    simulation = Simulation(width, height)

    while True:
        print("\nPlease choose from the following options : ")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        print("[3] Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Please enter the name of the car: ").strip()
            x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
            commands = input(f"Please enter the commands for car {name}: ").strip()
            simulation.add_car(name, int(x), int(y), direction, commands)
        elif choice == "2":
            simulation.run()
        elif choice == "3":
            print("Thank you for running the simulation. byebye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
