class Ride:
    def __init__(self, start_location, finish_location, start_time, finish_time):
        self.start_location = start_location
        self.finish_location = finish_location
        self.start_time = start_time
        self.finish_time = finish_time

    def __str__(self):
        return "RIDE: from " + str(self.start_location) + " at " + str(self.start_time) + " to " + str(self.finish_location) + " at " + str(self.finish_time)
