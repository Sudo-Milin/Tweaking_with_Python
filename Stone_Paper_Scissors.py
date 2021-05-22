import random

# -----Global variables-----
list_of_valid_inputs = ["stone","paper","scissors"]

# Checks all the winning coditions of Stone-paper-Scissors game
def check_win_condition(choice_1, choice_2):
    if choice_1 == "stone" and choice_2 == "paper":
        # Paper wraps the Stone
        return print(choice_2 +" wins!!")
    elif (choice_1 == "stone" and choice_2 == "scissors"):
        # Stone breaks the Scissors
        return print(choice_1 +" wins!!")
    elif choice_1 == "paper" and choice_2 == "scissors":
        # Scissors cuts the Paper
        return print(choice_2 +" wins!!")
    elif choice_1 == "paper" and choice_2 == "stone":
        # Paper wraps the Stone
        return print(choice_1 +" wins!!")
    elif choice_1 == "scissors" and choice_2 == "stone":
        # Stone breaks the Scissors
        return print(choice_2 +" wins!!")
    elif choice_1 == "scissors" and choice_2 == "paper":
        # Scissors cuts the Paper
        return print(choice_1 +" wins!!")
    
            

# The complete game play
def play_game():

    # Setup global variables
    global list_of_valid_inputs
    user_choice = input(str("Enter your choice (Stone-Paper-Scissors): "))
    computer_choice = random.choice(list_of_valid_inputs)
    if user_choice in list_of_valid_inputs:
        print("Your choice = {a} and Computer choice = {b}".format(a=user_choice, b=computer_choice))
        if user_choice == computer_choice:
            print("Its a TIE!!")            
        check_win_condition(user_choice, computer_choice)
    else:
        print("Invalid input !! Please input correct choice. (Stone-Paper-Scissors)")

# Game Starts
while True:
    play_game()


