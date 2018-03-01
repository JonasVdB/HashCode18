from Location import Location
from Ride import Ride

class InputParser:
    def __init__(self):
        self.ridelist = list()



    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        param = firstline[:-1].split(' ')
        num_rows, num_cols, num_vehicles, num_rides, bonus, simsteps = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4]), int(param[4])

        for id in range(num_rides):
            rideline = inputfile.readline()
            param = rideline[:-1].split(' ')
            row, col, fin_row, fin_col, start, finish = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4]), int(param[5])
            start_location = Location(row, col)
            finish_location = Location(fin_row, fin_col)
            ride = Ride(id, start_location, finish_location, start, finish)
            self.ridelist.append(ride)
            print(ride)

        return self.ridelist, bonus, simsteps, num_rows, num_cols, num_vehicles
