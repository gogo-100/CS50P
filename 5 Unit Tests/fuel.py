def main():
    while True:
        fraction = input("Fraction: ")
        x = convert(fraction)
        if x is None:
            continue
        else:
            gauge(x)

def convert(fraction):
    try:
        a,b =fraction.split("/")
        x = round(int(a) / int(b) *100)
        if int(a) > int(b):
            raise ValueError
        else:
            return x
    except:
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()