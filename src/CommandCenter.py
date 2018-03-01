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
        self.initcars()


    def planCars(self):
        for time in range(self.simTime):
            carsAvailable = self.cardict[time]

            for car in carsAvailable:

                car = self.planRideForCar(car)
                if car is not None:

                    self.cardict[car.timeAvailable].append(car)

            self.cardict[time]= list()


    def initcars(self):
        for car in self.cars:

            self.planRideForCar(car)
            self.cardict[car.timeAvailable].append(car)



    def planRideForCar(self,car):

        # Select a ride to add to the car
        selected_ride = self.findClosestRide(car.currentLocation, car.timeAvailable, self.rides)
        if selected_ride is None:
            return None
        # add the ride to the car
        car.addNewRide(selected_ride)
        self.rides.remove(selected_ride)

        return car

    def findClosestRide(self,carLocation,currentTime,rides):
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