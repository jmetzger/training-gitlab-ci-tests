import pytest
from calculator import add, subtract, multiply, divide, is_even


def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_float():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division durch Null"):
        divide(5, 0)

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False
