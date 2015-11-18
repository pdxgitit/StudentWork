import random

n = True
while n:

    counter = 0
    numbers_str = str(random.randint(10000, 19999))[1:5]
    m = True

    print("Welcome to cows and bulls game.\nIf you want to quit type 'exit'")

    while m:

        guess = input("Guess our 4 digit number: ")

        if guess == 'exit':
            n = False
            break

        elif len(guess) != 4:
            print("Wrong input!")
            continue

        cows = len([numbers_str[i] for i in range(len(numbers_str)) if numbers_str[i] == guess[i]])
        s = len([num for num in numbers_str if num in guess])
        bulls = s - cows

        if cows == len(numbers_str):
            counter += 1
            print("Congratulations you predicted in %d tries." % counter)
            m = False
        else:
            counter += 1
            print("You have " + str(cows) + " cows and " + str(bulls) + " bulls.")
