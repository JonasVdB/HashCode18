from InputParser import InputParser

def process_file(filename):
    parser = InputParser()
    parser.parse("../input/" + filename + ".in")


    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write("TEST")

if __name__ == "__main__":
    files = ["a", "b"]
    #files = ["a", "b", "c", "d", "e"]
    for file in files:
        print("starting file: "+file)
        process_file(file)