import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-3:]!=".py":
    sys.exit("Not a Python file")

try:
    count = 0
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or line.isspace() or line == '':
                continue
            else:
                count += 1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")