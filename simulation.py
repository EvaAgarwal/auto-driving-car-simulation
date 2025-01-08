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
        self.cars.append({"car": Car(name, x, y, direction), "commands": commands})

    def run(self):
        steps = 0
        while any(car_info['commands'] for car_info in self.cars):
            steps += 1
            for car_info in self.cars:
                car = car_info['car']
                if not car_info['commands']:
                    continue
                command = car_info['commands'][0]
                car_info['commands'] = car_info['commands'][1:]
                if command == 'L':
                    car.rotate_left()
                elif command == 'R':
                    car.rotate_right()
                elif command == 'F':
                    car.move()
                    if not (0 <= car.x < self.width and 0 <= car.y < self.height):
                        print(f"{car.name} hit the boundary at step {steps}.")
                        car.move()  # Undo move
                for other in self.cars:
                    if other is car_info:
                        continue
                    other_car = other['car']
                    if car.x == other_car.x and car.y == other_car.y:
                        print(f"Collision: {car.name} collided with {other_car.name} at step {steps}.")
                        return
        self.print_results()

    def print_results(self):
        print("\nAfter simulation, the result is:")
        for car_info in self.cars:
            car = car_info['car']
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
