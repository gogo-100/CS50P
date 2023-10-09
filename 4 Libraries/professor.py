import random

def main():
    level = pow(10,get_level())
    count = 10
    score = 0
    error = 0
    while count > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            if error == 3:
                print(f"{x} + {y} = {x+y}")
                error = 0
                break
            ans = input(f"{x} + {y} = ")
            if ans.isnumeric() and int(ans) == x + y:
                score += 1
                break
            else:
                print("EEE")
                error += 1
        count -= 1
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            level = input("Level: ").strip()
            if level.isnumeric() and int(level) >= 1 and int(level) <= 3:
                return int(level)
            else:
                raise ValueError
        except:
            pass

def generate_integer(level):
    if level == 10:
        return random.randint(level/10-1,level)
    else:
        return random.randint(level/10,level)

if __name__ == "__main__":
    main()