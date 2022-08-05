import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.Calculator = Calculator

    def test_sum(self):
        self.assertEqual(self.Calculator(1, 2).sum(), 3)
        self.assertEqual(self.Calculator('adsf', 2).sum(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').sum(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').sum(), 'переменные могут быть только числового типа(int, float)')

    def test_sub(self):
        self.assertEqual(self.Calculator(1, 2).sub(), -1)
        self.assertEqual(self.Calculator('adsf', 2).sub(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').sub(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').sub(), 'переменные могут быть только числового типа(int, float)')

    def test_div(self):
        self.assertEqual(self.Calculator(2, 2).div(), 1)
        self.assertEqual(self.Calculator('adsf', 2).div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(2, 0).div(), 'Деление на ноль! Аргумент b не может быть равен нулю!')

    def test_mul(self):
        self.assertEqual(self.Calculator(1, 2).mul(), 2)
        self.assertEqual(self.Calculator(-1, 2).mul(), -2)
        self.assertEqual(self.Calculator(-1, 0).mul(), 0)
        self.assertEqual(self.Calculator('adsf', 2).div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').div(), 'переменные могут быть только числового типа(int, float)')


if __name__ == '__main__':
    unittest.main()
