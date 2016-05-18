#Skal ta imot json-fil

import json

#Datafiler kommer inn på formatet {"navn":"verdi"}

class TripData():
  #  fuel_used
   # distance
    #duration = 0
    def __init__(self):
        self.fuel_used = 10
        self.distance = 100
        self.duration = 60

    def get_fuel_used(self):
        return self.fuel_used
    def get_distance(self):
        return self.distance
    def get_duration(self):
        return self.duration

