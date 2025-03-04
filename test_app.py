import unittest
from app import add, subtract, multiply, divide, percentage

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1.5, 2), 3.0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 0), "Error! Division by zero.")
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(7.5, 2.5), 3.0)

    def test_percentage(self):
        self.assertEqual(percentage(50, 100), 50)
        self.assertEqual(percentage(25, 100), 25)
        self.assertEqual(percentage(0, 100), 0)
        self.assertEqual(percentage(50, 0), "Error! Division by zero.")
        self.assertEqual(percentage(75, 150), 50)

if __name__ == '__main__':
    unittest.main()