import random


def guesser(low, high, ans):
    global counter
    counter += 1
    while True:
        guess = input("Guess the hidden number: ")
        if guess.isdigit():
            guess = int(guess)
            if low <= guess <= high:
                if guess < ans:
                    print("Try higher!")
                    return guesser(guess + 1, high, ans)
                elif guess > ans:
                    print("Try lower!")
                    return guesser(low, guess - 1, ans)
                else:
                    print("Correct!")
                    print(f'Number of guesses: {counter}')
                    break
            else:
                print("Your guess must be between the latest min and max numbers")
                continue
        else:
            print("Invalid input! Please try again")
            continue


def chooser(low, high):
    global counter
    counter += 1
    guess = random.randint(low, high)
    while True:
        answer = input(f'Is {guess} lower (l) or higher (h) or a correct (c) number? ')
        if answer.lower() == "l":
            return chooser(guess + 1, high)
        elif answer.lower() == "h":
            return chooser(low, guess - 1)
        elif answer.lower() == "c":
            print("Yay!")
            print(f'Number of guesses: {counter}')
            break
        else:
            print("Invalid input! Please try again!")
            continue


def new_game():
    print("Welcome to Guess The Number! Please choose an option:")
    print("1. Be the guesser")
    print("2. Be the chooser")
    while True:
        choice = input("Enter your option: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in [1, 2]:
                break
            else:
                print("Your answer must be 1 or 2.")
                continue
        else:
            print("Your answer must be 1 or 2.")
            continue

    while True:
        print("Pick the limit numbers")
        min_num = input("Min: ")
        max_num = input("Max: ")
        if min_num.isdigit() and max_num.isdigit():
            min_num = int(min_num)
            max_num = int(max_num)
            if min_num < max_num:
                break
            else:
                print("Min must be lower than Max number.")
                continue
        else:
            print("Invalid input! Please try again!")
            continue

    answer = random.randint(min_num, max_num)
    if choice == 1:
        guesser(min_num, max_num, answer)
    if choice == 2:
        print(f'Think of a number between {min_num} and {max_num} ')
        print("Computer will guess what your chosen number is.")
        chooser(min_num, max_num)


counter = 0

while True:
    new_game()
    cont = input("Do you want to try again? ")
    if cont.lower() == "yes":
        continue
    else:
        break
print("Thank you for playing! Have a nice day!")