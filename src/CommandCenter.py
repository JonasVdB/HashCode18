from Location import Location
class CommandCenter:
    def __init__(self, rides, simTime, car_amount, bonus ):
        # type: (object, object, object, object) -> object
        self.rides = rides
        self.cars = list()
        self.simTime = 0

    def planAllCars(self):
        for car in self.cars:
            self.planCar(car)

    def planCar(self, car):
        time = 0
        location = Location(0,0)
        while time<=self.simTime:
            #Select a ride to add to the car
            selected_ride = self.findClosestRide(location,time,self.rides,self.simTime)
            if selected_ride is None:
                break
            #add the ride to the car
            car.addNewRide(selected_ride)
            self.rides.remove(selected_ride)

            #adjust the simulation time
            time += self.travelTime(location,selected_ride.start_location)
            if time<selected_ride.start_time:
                time = selected_ride.start_time
            time += self.travelTime(selected_ride.start_location, selected_ride.finish_location)


    @staticmethod
    def travelTime(loc1, loc2):
        return

    def findClosestRide(self,carLocation,currentTime,rides,maxSimTime):
        return

    def getOutput(self):
        output = ""
        for car in self.cars:
            output += car.output() + "\n"
        return output