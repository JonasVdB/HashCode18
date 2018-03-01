from InputParser import InputParser
from CommandCenter import CommandCenter

def process_file(filename):
    parser = InputParser()
    ridelist, bonus, simsteps, num_rows, num_cols, cars= parser.parse("../input/" + filename + ".in")



    cmd = CommandCenter(ridelist, simsteps, cars, bonus)

    cmd.planCars()

    output = cmd.getOutput()
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(output)

if __name__ == "__main__":

    files = ["a", "b", "c", "d", "e"]

    for file in files:
        print("starting file: "+file)
        process_file(file)