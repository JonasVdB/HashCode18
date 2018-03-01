class Location:
    def __init__(self,row, col):
        self.col = col
        self.row = row

    def __str__(self):
        return "<"+str(self.row) + "," + str(self.col) + ">"

