# Using DataStream to calculate different scores
import Trip

class fuel_usage_score():

    def __init__(self):
        self.fuel_used=Trip.TripData.get_fuel_used()
        self.distance=Trip.TripData.get_distance()

    def get_score(self):
        return self.fuel_used/self.distance
    