from datetime import date
import inflect,sys

def main():
    birth = input("Date of Birth: ")
    print(convert(birth))

def convert(birth):
    try:
        time2 = date.fromisoformat(birth)
    except:
        sys.exit("Invalid date")
    time1 = date.today()
    mins = (time1-time2).days*60*24
    p = inflect.engine()
    return p.number_to_words(mins,andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()