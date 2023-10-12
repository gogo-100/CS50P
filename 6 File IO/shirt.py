import sys

from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) == 4:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith((".jpeg",".jpg",".png")) or not sys.argv[2].endswith((".jpeg",".jpg",".png")):
    sys.exit("Invalid output")

if sys.argv[1][-4:] != sys.argv[2][-4:]:
    sys.exit("Input and output have different extensions")


try:
    shirt = Image.open("shirt.png")
    person = Image.open(sys.argv[1])
    size = shirt.size
    person = ImageOps.fit(person,size)
    person.paste(shirt, shirt)
    person.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("Input does not exist")