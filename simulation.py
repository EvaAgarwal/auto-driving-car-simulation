from car import Car

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, name, x, y, direction, commands):
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Error: Initial position is out of bounds.")
            return
        for car_info in self.cars:
            if car_info['car'].x == x and car_info['car'].y == y:
                print(f"Error: Position ({x},{y}) is already occupied by another car.")
                return
        self.cars.append({"car": Car(name, x, y, direction), "commands": commands})

    def run(self):
        steps = 0
        active = True

        while active:
            steps += 1
            active = False  # Check if there are still commands to process

            for car_info in self.cars:
                car = car_info['car']
                if not car_info['commands']:
                    continue  # Skip cars with no commands left

                active = True
                command = car_info['commands'][0]  # Fetch the next command
                car_info['commands'] = car_info['commands'][1:]  # Remove processed command

                if command == 'L':
                    car.rotate_left()
                elif command == 'R':
                    car.rotate_right()
                elif command == 'F':
                    old_x, old_y = car.x, car.y  # Save current position
                    car.move()
                    
                    # Check for boundary collision
                    if not (0 <= car.x < self.width and 0 <= car.y < self.height):
                        print(f"{car.name} hit the boundary at step {steps}.")
                        car.x, car.y = old_x, old_y  # Undo the move
                        continue

                    # Check for collisions with other cars
                    for other_info in self.cars:
                        other_car = other_info['car']
                        if other_car == car:  # Skip self-check
                            continue
                        if car.x == other_car.x and car.y == other_car.y:
                            print(f"Collision: {car.name} collided with {other_car.name} at step {steps}.")
                            return

        self.print_results()

    def print_results(self):
        print("\nAfter simulation, the result is:")
        for car_info in self.cars:
            car = car_info['car']
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
