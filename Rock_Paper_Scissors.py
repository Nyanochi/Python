import random

def new_game():
    win = bool
    while True:
        choices = ["rock","paper","scissors"]
        computer_choice = random.choice(choices)
        while True:
            your_choice = input("Please choose Rock, Paper or Scissors: ")
            if your_choice.lower() not in choices:
                print("Invalid input. Please choose again!")
                continue
            else:
                break
        print(f'You choose: {your_choice:^5}. Computer chooses: {computer_choice:^5}')
        if (your_choice == "rock" and computer_choice == "scissors") or \
            (your_choice == "paper" and computer_choice == "rock") or \
            (your_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            win = True
            break
        elif (your_choice == "rock" and computer_choice == "paper") or \
            (your_choice == "paper" and computer_choice == "scissors") or \
            (your_choice == "scissors" and computer_choice == "rock"):
            print("You lose!")
            win = False
            break
        else:
            print("Tie! Again.")
            continue
    return win

computer_score = your_score = 0

while True:
    print("Welcome to Rock, Paper & Scissors The Game")
    if new_game():
        your_score += 1
    else:
        computer_score += 1
    cont = input("Do you want to continue? ")
    if cont.lower() == "yes":
        continue
    else:
        break
print(f'Computer: {computer_score}, You: {your_score}')
if computer_score > your_score:
    print("You lost the game!")
elif computer_score < your_score:
    print("You won the game!")
else:
    print("Tie")
print("Thank you for playing! Have a nice day!")