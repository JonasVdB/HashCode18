class CommandCenter:
    def __init__(self):
        self.rides = list()
        self.cars = list()

    def planAllCars(self):
        for car in self.cars:
            self.planCar(car)

    def planCar(self, car):
        time = 0
        location = Location(0,0)