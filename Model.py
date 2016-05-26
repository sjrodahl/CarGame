# Using DataStream to calculate different scores
import Trip
import math

class Algorithms():

    def __init__(self):
        self.trip = Trip.TripData()
        self.fuel_used=self.trip.fuel_used_since_restart
        self.distance=self.trip.distance_since_restart
        self.duration=self.trip.duration_since_restart

    def average_fuel_consumption(self):
        return self.fuel_used/self.distance

    def fuel_usage_score(self):
        return self.average_fuel_consumption()*math.log(self.duration, math.e)


