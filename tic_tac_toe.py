# Tic-Tac-Toe game
# Plays the game of tic-tac-toe against a human opponent


# golbal constants

X = "X" # One of the entry from either computer or human
o = "o" # Same as X description
EMPTY = " " # Represents a square on the board
TIE = "TIE" # Once a user draw the match this value will be printed
NUM_SQUARES = 9 # represents the number of the squares on the board


# the display_instruct() function
def display_instruct():
    """Display game instructions"""
    print(
        """
            Welcome to the greatest intellectual challenge of all the time:
            This will be a showdown between your human brain and a computer.
            
            You will make your move known by entering a number, 0-8. The
            number will correspond to the board position as illustrated.
                                0 | 1 | 2 |
                                -----------
                                3 | 4 | 5 |
                                -----------
                                6 | 7 | 8 |
            
            Prepare yourself, human.
        """
    )

# The ask_yes_no() function
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


# The ask_number() function
def ask_number(question, low, high):
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move ? (y/n):")
    if go_first == "y":
        print("\n Then take the first move. You will need it.")
        human = X
        computer = o
    else:
        print("\n Your bravery will be your undoing... I will go first.")
        computer = X
        human = o
    return computer, human

# Notice that this function calls one of the previously created function
# That is totally fine. It can.

# The new_board() function
def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


# The diplay_board() Function
def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])


# main
z = new_board()
display_board(z)