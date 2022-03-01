#test_vehicle.py
import pytest
from Vehicle import Vehicle

def test_lowco2_vehicle():
    myVehicle = Vehicle("192D1122","Fiat","500", 88)
    assert myVehicle.__str__() == "192D1122 Fiat 500"
    assert myVehicle.get_annual_tax()==150

def test_highco2_vehicle():
    myVehicle = Vehicle("181D1133","Land Rover","Range Rover", 235)
    assert myVehicle.__str__() == "181D1133 Land Rover Range Rover"
    assert myVehicle.get_annual_tax()==200
