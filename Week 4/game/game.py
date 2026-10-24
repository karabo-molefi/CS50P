import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level > 0:
            if level <= 100:
                break

r = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > r:
            print("Too large!")
        elif guess < r:
            print("Too small!")
        else:
            print("Just right!")
            break