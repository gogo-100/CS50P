import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b",s.lower())
    if matches is None:
        return 0
    else:
        return len(matches)


if __name__ == "__main__":
    main()