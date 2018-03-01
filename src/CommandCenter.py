from Location import Location
from collections import defaultdict

class CommandCenter:
    def __init__(self, rides, simTime, cars, bonus ):
        # type: (object, object, object, object) -> object
        self.rides = rides
        self.cars = cars
        self.simTime = simTime
        self.bonus = bonus
        self.cardict = defaultdict(list)







    def planAllCars(self):
        for car in self.cars:
            self.planCar(car)

    def planCar(self, car):
        time = 0
        location = Location(0,0)
        while time <= self.simTime:
            #Select a ride to add to the car
            selected_ride = self.findClosestRide(location,time,self.rides,self.simTime)
            if selected_ride is None:

                break
            #add the ride to the car
            car.addNewRide(selected_ride)
            self.rides.remove(selected_ride)

            #adjust the simulation time
            time += Location.distance(location,selected_ride.start_location)  # go to start
            if time<selected_ride.start_time:
                time = selected_ride.start_time # waiting for ride to start
            time += Location.distance(selected_ride.start_location, selected_ride.finish_location) # finish ride




    def findClosestRide(self,carLocation,currentTime,rides,maxSimTime):
        best_ride = None
        best_ride_value = 0
        for ride in rides:
            if self.isFeasable(ride, carLocation, currentTime):
                ride_value = self.rideValue(ride,carLocation,currentTime)
                if ride_value > best_ride_value:
                    best_ride = ride
                    best_ride_value = ride_value
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
        duration_ride = value_ride + dist_to + wait_time

        if duration_ride == 0:
            return 0
        else:
            return (value_ride + bonus_value - dist_to - wait_time)*1.0/(duration_ride)


    def getOutput(self):
        output = ""
        for car in self.cars:
            output += car.output() + "\n"
        return output