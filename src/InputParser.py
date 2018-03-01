from Location import Location
from Ride import Ride
from Car import Car

class InputParser:
    def __init__(self):
        self.ridelist = list()
        self.carlist = list()



    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        param = firstline[:-1].split(' ')
        num_rows, num_cols, num_vehicles, num_rides, bonus, simsteps = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4]), int(param[5])

        for id in range(num_rides):
            rideline = inputfile.readline()
            param = rideline[:-1].split(' ')
            row, col, fin_row, fin_col, start, finish = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4]), int(param[5])
            start_location = Location(row, col)
            finish_location = Location(fin_row, fin_col)
            ride = Ride(id, start_location, finish_location, start, finish)
            self.ridelist.append(ride)

        for car_id in range(num_vehicles):
            car = Car(car_id)
            self.carlist.append(car)

        return self.ridelist, bonus, simsteps, num_rows, num_cols, self.carlist
