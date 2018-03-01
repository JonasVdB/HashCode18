from Location import Location

class CommandCenter:
    def __init__(self, rides, simTime, cars, bonus ):
        # type: (object, object, object, object) -> object
        self.rides = rides
        self.cars = cars
        self.simTime = 0
        self.bonus = 0

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
        best_ride = None
        best_ride_value = 0
        for ride in rides:
            if self.isFeasable(ride, carLocation, currentTime):
                ride_value = self.rideValue(ride,carLocation,currentTime)
                if ride_value > best_ride_value:
                    best_ride = ride
        return best_ride

    def isFeasable(self,ride, carLocation, currentTime):
        dist_to = Location.distance(carLocation,ride.start_location)
        dist_ride = Location.distance(ride.start_location,ride.finish_location)

        if (dist_to+dist_ride+currentTime<=ride.finish_time):
            return True
        else:
            return False


    def rideValue(self,ride, carLocation, currentTime):
        value_ride = Location.distance(ride.start_location,ride.finish_location)
        dist_to = Location.distance(carLocation,ride.start_location)
        if currentTime+ dist_to <= ride.start_time:
            bonus_value = self.bonus
        else:
            bonus_value = 0
        wait_time = ride.start_time - currentTime - dist_to

        return value_ride + bonus_value - dist_to - wait_time


    def getOutput(self):
        output = ""
        for car in self.cars:
            output += car.output() + "\n"
        return output