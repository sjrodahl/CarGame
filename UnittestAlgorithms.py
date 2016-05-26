import unittest
import Model
import Trip
import math
#Testdata:
FUEL_USED = 20  #liter
DISTANCE = 50   #km
DURATION= 40       #min

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.trip = Trip.TripData()
        self.algorithms = Model.Algorithms()
    def test_average_fuel_consumption(self):
        self.assertEqual(self.algorithms.average_fuel_consumption(), FUEL_USED/DISTANCE)
    def test_fuel_usage_score(self):
        self.assertEqual(self.algorithms.fuel_usage_score(), FUEL_USED/DISTANCE*math.log(DURATION, math.e))
