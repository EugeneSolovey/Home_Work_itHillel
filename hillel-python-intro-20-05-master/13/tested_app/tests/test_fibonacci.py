"""
Tests for fibbonaci calculation functions.
"""

from formulas.fibonacci import fibonacci


def test_fibonacci_0():
    """
    Test fibonacci function for 0.
    """
    assert fibonacci(0) == 0


def test_fibonacci_8():
    """
    Test fibonacci function for 8.
    """
    assert fibonacci(8) == 21
