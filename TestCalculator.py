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
        self.assertEqual(self.Calculator(1.2, 2).sum(), 3.2)
        self.assertEqual(self.Calculator(1, 2.123).sum(), 3.123)
        self.assertEqual(self.Calculator(1.125, 2.123).sum(), 3.248)
        self.assertEqual(self.Calculator('13', 1).sum(), 14)
        self.assertEqual(self.Calculator(1, '13').sum(), 14)
        self.assertEqual(self.Calculator('13', '1').sum(), 14)

    def test_sub(self):
        self.assertEqual(self.Calculator(1, 2).sub(), -1)
        self.assertEqual(self.Calculator('adsf', 2).sub(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').sub(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').sub(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(2, 1.2).sub(), 0.8)
        self.assertEqual(self.Calculator(2.96998, -1.3).sub(), 4.26998)
        self.assertEqual(self.Calculator('14', 1).sub(), 13)
        self.assertEqual(self.Calculator(1, '13').sub(), -12)
        self.assertEqual(self.Calculator('13', '1').sub(), 12)

    def test_div(self):
        self.assertEqual(self.Calculator(2, 2).div(), 1)
        self.assertEqual(self.Calculator('adsf', 2).div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(2, 0).div(), 'Деление на ноль! Аргумент b не может быть равен нулю!')
        self.assertEqual(self.Calculator(5.2, 2).div(), 2.6)
        self.assertEqual(self.Calculator(5, 2.5).div(), 2)
        self.assertEqual(self.Calculator('14', 2).div(), 7)
        self.assertEqual(self.Calculator(2, '13').div(), 2/13)
        self.assertEqual(self.Calculator('15', '5').div(), 3)


    def test_mul(self):
        self.assertEqual(self.Calculator(1, 2).mul(), 2)
        self.assertEqual(self.Calculator(-1, 2).mul(), -2)
        self.assertEqual(self.Calculator(-1, 0).mul(), 0)
        self.assertEqual(self.Calculator('adsf', 2).div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator(1, 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('bf', 'djfb').div(), 'переменные могут быть только числового типа(int, float)')
        self.assertEqual(self.Calculator('14', 1).mul(), 14)
        self.assertEqual(self.Calculator(1, '13').mul(), 13)
        self.assertEqual(self.Calculator('13', '2').mul(), 26)


if __name__ == '__main__':
    unittest.main()
