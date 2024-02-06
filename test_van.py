#test_van.py
import pytest
from Van import Van

def test_vehicle():
    myVan = Van("00D1122","Renault","Kango",75,100000)
    myVan.set_miles(10000)
    assert myVan.getMakeModel() == "Ford Mondeo"
    assert myVan.getMiles() == 100000
    assert myVan.getCapacity() == 75

