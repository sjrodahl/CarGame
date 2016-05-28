import unittest
import Model
import Trip
import math
#Testdata:
FUEL_USED = Trip.TripData.fuel_used_since_restart  #liter
DISTANCE = Trip.TripData.distance_since_restart   #km
DURATION= Trip.TripData.duration_since_restart       #min

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.trip = Trip.TripData()
        self.algorithms = Model.Algorithms()
        self.avg_fuel = FUEL_USED/DISTANCE

    def calculate_fuel_usage_score(self, fuel, dist, dur):
        return 1/(fuel/dist)*math.log(dur, math.e)

    def test_average_fuel_consumption(self):
        self.assertEqual(self.algorithms.average_fuel_consumption(), self.avg_fuel)
    def test_fuel_usage_score(self):
        self.assertEqual(self.algorithms.fuel_usage_score(), self.calculate_fuel_usage_score(FUEL_USED, DISTANCE, DURATION))
    def test_inverse_proportionality(self):
        new_fuel = FUEL_USED+10
        self.assertGreater(self.algorithms.fuel_usage_score(), self.calculate_fuel_usage_score(new_fuel, DISTANCE, DURATION))
        new_dist = DISTANCE+10
        self.assertLess(self.algorithms.fuel_usage_score(), self.calculate_fuel_usage_score(FUEL_USED,new_dist, DURATION))
        new_dur = DURATION+10
        self.assertLess(self.algorithms.fuel_usage_score(), self.calculate_fuel_usage_score(FUEL_USED, DISTANCE, new_dur))
