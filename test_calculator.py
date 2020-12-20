"""
Unit tests for the calculator library
"""

import calculator

class TestCalculator:
    """
    Class to test the calculator.py file
    """

    def test_addition(self):
        """ Test for the add function """
        assert calculator.add(1, 3) == 4

    def test_subtraction(self):
        """ Test for the subtract function """
        assert calculator.subtract(4, 2) == 2

    def test_multiplication(self):
        """ Test for the multiply function """
        assert calculator.multiply(10, 10) == 100
