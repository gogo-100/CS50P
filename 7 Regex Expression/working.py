import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.fullmatch(r"(.*?) (A|P)M to (.*?) (A|P)M", s)
    if matches is None:
        raise ValueError
    return convert12to24(matches.group(1),matches.group(2)) + " to " + convert12to24(matches.group(3),matches.group(4))

def convert12to24(time, part):
    index = time.find(":")
    hh = int(time) if index == -1 else int(time[:index])
    if part == "A" and hh == 12:
        hh = 0
    elif part == "P" and hh != 12 :
        hh += 12
    mm = 0 if index == -1 else int(time[index + 1:])
    if mm >= 60:
        raise ValueError
    return f"{hh:02}:{mm:02}"

if __name__ == "__main__":
    main()