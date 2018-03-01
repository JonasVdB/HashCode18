from Location import Location

class Car:

    def __init__(self, id):
        self.rides = list()
        self.id = id
        self.timeAvaliable = 0
        self.currentLocation = Location(0,0)


    def addNewRide(self,ride):
        self.rides.append(ride)
        self.currentLocation = ride.finish_location
        self.timeAvaliable

    def output(self):
        output = ""
        for ride in self.rides:
            output += str(ride.id)
            output += " "
        if output != "":
            output = output[:-1]
        return str(len(self.rides)) + " " + output


    def __str__(self):
        return str(self.id)