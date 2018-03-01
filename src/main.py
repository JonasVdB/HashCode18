from InputParser import InputParser
from CommandCenter import CommandCenter

def process_file(filename):
    parser = InputParser()
    ridelist, bonus, simsteps, num_rows, num_cols, num_vehicles= parser.parse("../input/" + filename + ".in")

    cmd = CommandCenter(ridelist, simsteps, num_vehicles, bonus)

    output = cmd.getOutput()
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(output)

if __name__ == "__main__":
    files = ["a", "b"]
    #files = ["a", "b", "c", "d", "e"]
    for file in files:
        print("starting file: "+file)
        process_file(file)