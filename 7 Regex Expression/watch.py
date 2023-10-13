import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'youtube.com/embed/(.*?)"', s)
    if matches is not None:
        return "https://youtu.be/" + matches.group(1)
    return matches

if __name__ == "__main__":
    main()