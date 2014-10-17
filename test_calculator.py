from unittest import TestCase
from Calculator import *
__author__ = 'jpflorido'


class TestCalculator(TestCase):
    def test_suma(self):
        my_calc = Calculator(2, 4)
        self.assertEqual(my_calc.suma(), 6)

    def test_resta(self):
        my_calc = Calculator(2, -3)
        self.assertEqual(my_calc.resta(), 5)

    def test_multiplicacion(self):
        my_calc = Calculator(2, 3)
        self.assertEqual(my_calc.multiplicacion(), 6)

    def test_division(self):
         my_calc = Calculator(2, 4)
         self.assertEqual(my_calc.division(), 0.5)