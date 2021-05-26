#----Global Variables-------

# If game is still going
game_still_going = True

# Who won? OR tie?
winner = None

# Whose turn?
current_player = "X"

# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"] 

# Display initial board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])   
    print(board[3] + " | " + board[4] + " | " + board[5])   
    print(board[6] + " | " + board[7] + " | " + board[8])  


# Game starts
def play_game():
    
    # Display initial board
    display_board()

    while game_still_going:
        
        # Handle a single turn of current player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Change to the other player
        flip_player()


    # At the game's end
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")


# Handle a single turn of current player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    # validation flag used to avoid overwritting of the inputs
    valid = False
    # Ensure that the player inputs the correct input and at correct position 
    while not valid:   
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        
        position = int(position) - 1
        
        # Only accept input if there is '-' in the mentioned board position
        if board[position] == "-":
            valid = True
        else:
            print("You can't input in this position, choose again.")


    board[position] = player

    display_board() 

# Checks if the game is at end state (game over conditions)
def check_if_game_over():
    check_for_winner()
    check_if_tie()

# Checks for the winner of the game (X or O)
def check_for_winner():

    # Setup global variable
    global winner
    
    # Check row for winner
    row_winner = check_row()
    # Check column for winner
    colunm_winner = check_column()
    # Check diagonal for winner
    diagonal_winner = check_diagonal()

    # Get the winner
    if row_winner:
        winner = row_winner
    elif colunm_winner:
        winner = colunm_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# Check row for winner
def check_row():

    # Setup global variables
    global game_still_going

    # Check if any row have same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return a winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# Check column for winner
def check_column():

    # Setup global variables
    global game_still_going

    # Check if any column have same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return a winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

# Check diagonal for winner
def check_diagonal():
    
    # Setup global variables
    global game_still_going

    # Check if any diagonal have same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return a winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# Check if the game is a Tie
def check_if_tie():

    # Setup global variable
    global game_still_going

    # If there remains now '-' on the board the the game is a tie
    if "-" not in board:
        game_still_going = False
    return

# Flipping turn from player X to player O or vice versa
def flip_player():

    # Setup global variable
    global current_player

    # if the current player is x then change to o
    if current_player == "X":
        current_player = "O"
    # if the current player is o then change to x
    elif current_player == "O":
        current_player = "X"
    
    return


play_game()
