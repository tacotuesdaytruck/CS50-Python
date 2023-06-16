import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(count_lines(sys.argv[1]))

def count_lines(file):
    try:
        counter = 0
        with open(file, "r") as file:
            for line in file:
                if len(line.strip()) == 0:
                    continue
                if not line.strip().startswith("#"):
                    counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return counter

if __name__ == "__main__":
    main()
