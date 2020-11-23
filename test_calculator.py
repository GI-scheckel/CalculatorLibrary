"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    """
    Class to test the calculator.py file
    """

    def test_addition(self):
        assert calculator.add(1, 3) == 4 

    def test_subtraction(self):
        assert calculator.subtract(4, 2) == 2 

    def test_multiplication(self):
        assert calculator.multiply(10, 10) == 100 
