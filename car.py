class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1

    def rotate_left(self):
        idx = (self.DIRECTIONS.index(self.direction) - 1) % 4
        self.direction = self.DIRECTIONS[idx]

    def rotate_right(self):
        idx = (self.DIRECTIONS.index(self.direction) + 1) % 4
        self.direction = self.DIRECTIONS[idx]
