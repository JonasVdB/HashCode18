class Location:
    def __init__(self,row, col):
        self.col = col
        self.row = row

    def distance(self, otherlocation):
        x = self.col - otherlocation.col
        y = self.row - otherlocation.row
        dist = abs(x) + abs(y)
        return dist

    def __str__(self):
        return "<"+str(self.row) + "," + str(self.col) + ">"

