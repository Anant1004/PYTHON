import random

def take_user_input():
    user_input = input("Enter your choice - ROCK / PAPER / SCISSOR :\n ").upper()
    if user_input in ["ROCK", "PAPER", "SCISSOR"]:
        return user_input
    else:
        print("ERROR: INVALID COMMAND")

def computer_input():
    choices = ["ROCK", "PAPER", "SCISSOR"]
    return random.choice(choices)

def comparison(user_input, computer_choice):
    if user_input == computer_choice:
        print("TIE UP!!!")
    elif (
        (user_input == "ROCK" and computer_choice == "SCISSOR") or
        (user_input == "PAPER" and computer_choice == "ROCK") or
        (user_input == "SCISSOR" and computer_choice == "PAPER")
    ):
        print("!!!YOU WON!!!")
    else:
        print("ALAS!! YOU LOST")

def play_game():
    while True:
        print("Welcome to Rock, Paper, Scissors game")
        inputted_cmd = take_user_input()
        if inputted_cmd == "EXIT":
            break
        else :
            computer_choice = computer_input()
            print(f"You choose: {inputted_cmd}")
            print(f"Computer choose: {computer_choice}")
            if comparison(inputted_cmd, computer_choice):
                break

play_game()
