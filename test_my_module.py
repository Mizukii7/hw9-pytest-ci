import pytest
from my_module import factorial

def test_factorial_basic():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)