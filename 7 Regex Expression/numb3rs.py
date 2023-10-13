import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.fullmatch(r"([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})", ip)
    if matches:
        for i in range(4):
            if 255 < int(matches.group(i+1)) or 0 > int(matches.group(i+1)):
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()