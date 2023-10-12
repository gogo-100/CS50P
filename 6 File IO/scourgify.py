import sys, csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) == 4:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:]!=".csv":
    sys.exit("Not a CSV file")

res = []

try:
    with open(sys.argv[1], newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "name":
                continue
            last,first = row[0].split(",")
            res.append([first.strip(), last.strip(), row[1]])

    with open(sys.argv[2], "w") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "house"])
        for row in res:
            writer.writerow(row)


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")