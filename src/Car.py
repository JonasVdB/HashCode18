class Car:

    def __init__(self, id):
        self.rides = list()
        self.id = id

    def addNewRide(self,ride):
        self.rides.append(ride)

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