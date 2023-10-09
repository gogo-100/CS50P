def main():
    str = input("What time is it? ").lower().strip()
    time = convert(str)

    if time >=7 and time <=8:
        print("breakfast time")
    elif time >=12 and time <=13:
        print("lunch time")
    elif time >=18 and time <=19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes)/60


if __name__ == "__main__":
    main()