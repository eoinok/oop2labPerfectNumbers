#test_divisor.py
import pytest
from divisors import divisors

def test_divisors():
    divisorList = [1,2,4,7,14]
    assert divisors(28) == divisorList
