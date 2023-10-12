import sys, csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:]!=".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], newline='') as csvfile:
        read = csv.reader(csvfile)
        text = []
        for row in read:
            text.append(row)
        print(tabulate(text[1:], text[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")