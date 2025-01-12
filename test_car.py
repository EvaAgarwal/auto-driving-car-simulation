import unittest
from car import Car

class TestCar(unittest.TestCase):
    def test_move(self):
        car = Car("A", 0, 0, "N")
        car.move()
        self.assertEqual((car.x, car.y), (0, 1))

    def test_rotate_left(self):
        car = Car("A", 0, 0, "N")
        car.rotate_left()
        self.assertEqual(car.direction, "W")

    def test_rotate_right(self):
        car = Car("A", 0, 0, "N")
        car.rotate_right()
        self.assertEqual(car.direction, "E")


if __name__ == "__main__":
    unittest.main()
