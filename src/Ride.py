class Ride:
    def __init__(self,id, start_location, finish_location, start_time, finish_time):
        self.id = id
        self.start_location = start_location
        self.finish_location = finish_location
        self.start_time = start_time
        self.finish_time = finish_time

    def distance(self):
        return self.start_location.distance(self.finish_location)

    def __str__(self):
        return "RIDE: from " + str(self.start_location) + " at " + str(self.start_time) + " to " + str(self.finish_location) + " at " + str(self.finish_time)
