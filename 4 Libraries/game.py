import random

while True:
    level = input("Level: ").strip()
    if level.isnumeric() and int(level) > 0:
        level = random.randint(1,int(level))
        break

while True:
    guess = input("Guess: ").strip()
    if not guess.isnumeric() or int(guess) < 0:
        continue
    guess = int(guess)
    if guess < level:
        print("Too small!")
    elif guess > level:
        print("Too large!")
    else:
        print("Just right!")
        break