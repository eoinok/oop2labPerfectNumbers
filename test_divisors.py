#test_divisor.py
#import pytest
from divisors import divisors

def test_divisors_of_30():
    assert divisors(30) == [1, 2, 3, 5, 6, 10]
