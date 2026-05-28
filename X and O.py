import random
from time import sleep

# Xs and Os

RED    = "\033[31m"
BLUE   = "\033[34m"
WHITE  = "\033[37m"
YELLOW = "\033[33m"
CLEAR  = "\033[H\033[2J"

X = RED  + "X" + WHITE
O = BLUE + "O" + WHITE

VALID_INPUTS = ["top left", "top", "top right", "left", "middle", "right", "bottom left", "bottom", "bottom right"]
remaining_inputs = ["top left", "top", "top right", "left", "middle", "right", "bottom left", "bottom", "bottom right"]


print(YELLOW + "The following are the valid inputs for placing your " + X + YELLOW + " or " + O + YELLOW + " on the board:")
print(YELLOW + "top left, top, top right, left, middle, right, bottom left, bottom, bottom right" + WHITE)


last_player1 = O

turn    = X
round   = 1
playing = True

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

X_talley = 0
O_talley = 0

"┃"
"┃┃"
"┃┃┃"
"┃┃┃┃"
"╋╋╋╋"

def print_X_talley():
    global X_talley
    X_counter = X_talley
    while X_counter > 0:
        if X_counter > 25:
            print(RED + " " + str(X_counter), end="")
            X_counter = 0
        if X_counter >= 5:
            print(RED + " ╋╋╋╋", end="")
            X_counter -= 5
        elif X_counter == 4:
            print(RED + " ┃┃┃┃", end="")
            X_counter -= 4
        elif X_counter == 3:
            print(RED + " ┃┃┃", end="")
            X_counter -= 3
        elif X_counter == 2:
            print(RED + " ┃┃", end="")
            X_counter -= 2
        elif X_counter == 1:
            print(RED + " ┃", end="")
            X_counter -= 1
    print(WHITE)


def print_O_talley():
    global O_talley
    O_counter = O_talley
    while O_counter > 0:
        if O_counter > 25:
            print(BLUE + " " + str(O_counter), end="")
            O_counter = 0
        if O_counter >= 5:
            print(BLUE + " ╋╋╋╋", end="")
            O_counter -= 5
        elif O_counter == 4:
            print(BLUE + " ┃┃┃┃", end="")
            O_counter -= 4
        elif O_counter == 3:
            print(BLUE + " ┃┃┃", end="")
            O_counter -= 3
        elif O_counter == 2:
            print(BLUE + " ┃┃", end="")
            O_counter -= 2
        elif O_counter == 1:
            print(BLUE + " ┃", end="")
            O_counter -= 1
    print(WHITE)








def reset_everything():
    global turn, round, playing, board, last_player1, remaining_inputs
    if check_win() != None:
        if check_win() == X:
            turn = O
            last_player1 = O
        if check_win() == O:
            turn = X
            last_player1 = X
    else:
        if last_player1 == X:
            turn = O
            last_player1 = O
        if last_player1 == O:
            turn = X
            last_player1 = X
    round   = 1
    playing = True
    board   = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    remaining_inputs = ["top left", "top", "top right", "left", "middle", "right", "bottom left", "bottom", "bottom right"]

def check_top_horizontal_win():
    global board
    if board[0] == X and board[1] == X and board[2] == X:
        return X
    if board[0] == O and board[1] == O and board[2] == O:
        return O
    return None

def check_middle_horizontal_win():
    global board
    if board[3] == X and board[4] == X and board[5] == X:
        return X
    if board[3] == O and board[4] == O and board[5] == O:
        return O
    return None

def check_bottom_horizontal_win():
    global board
    if board[6] == X and board[7] == X and board[8] == X:
        return X
    if board[6] == O and board[7] == O and board[8] == O:
        return O
    return None

def check_left_vertical_win():
    global board
    if board[0] == X and board[3] == X and board[6] == X:
        return X
    if board[0] == O and board[3] == O and board[6] == O:
        return O
    return None

def check_middle_vertical_win():
    global board
    if board[1] == X and board[4] == X and board[7] == X:
        return X
    if board[1] == O and board[4] == O and board[7] == O:
        return O
    return None

def check_right_vertical_win():
    global board
    if board[2] == X and board[5] == X and board[8] == X:
        return X
    if board[2] == O and board[5] == O and board[8] == O:
        return O
    return None

def check_solidus_win():
    global board
    if board[0] == X and board[4] == X and board[8] == X:
        return X
    if board[0] == O and board[4] == O and board[8] == O:
        return O
    return None

def check_hack_win():
    global board
    if board[2] == X and board[4] == X and board[6] == X:
        return X
    if board[2] == O and board[4] == O and board[6] == O:
        return O
    return None

def check_win():
    global board
    # top horizontal win
    top_horizontal    = None
    top_horizontal    = check_top_horizontal_win()
    # middle horizontal win
    middle_horizontal = None
    middle_horizontal = check_middle_horizontal_win()
    # bottom horizontal win
    bottom_horizontal = None
    bottom_horizontal = check_bottom_horizontal_win()
    # left vertical win
    left_vertical     = None
    left_vertical     = check_left_vertical_win()
    # middle vertical win
    middle_vertical   = None
    middle_vertical   = check_middle_vertical_win()
    # right vertical win
    right_vertical    = None
    right_vertical    = check_right_vertical_win()
    # solidus win
    solidus           = None
    solidus           = check_solidus_win()
    # hack win
    hack              = None
    hack              = check_hack_win()
    if top_horizontal == None and middle_horizontal == None and bottom_horizontal == None and left_vertical == None and middle_vertical == None and right_vertical == None and solidus == None and hack == None:
        return None
    if top_horizontal == X or middle_horizontal == X or bottom_horizontal == X or left_vertical == X or middle_vertical == X or right_vertical == X or solidus == X or hack == X:
        return X
    if top_horizontal == O or middle_horizontal == O or bottom_horizontal == O or left_vertical == O or middle_vertical == O or right_vertical == O or solidus == O or hack == O:
        return O
    
def check_draw():
    global board
    if board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " ":
        if check_win() == None:
            return True
    return False




def print_board():
    print("round " + str(round))
    print(board[0] + " ┃ " + board[1] + " ┃ " + board[2])
    print("━━╋━━━╋━━", end=""); print_X_talley()
    print(board[3] + " ┃ " + board[4] + " ┃ " + board[5])
    print("━━╋━━━╋━━", end=""); print_O_talley()
    print(board[6] + " ┃ " + board[7] + " ┃ " + board[8])



def get_input():
    global turn
    global round
    global remaining_inputs
    VALID_INPUTS = ["top left", "top", "top right", "left", "middle", "right", "bottom left", "bottom", "bottom right"]
    user_input = None
    if turn == X:
        while user_input not in remaining_inputs:
            user_input = input(X + " to move: ")
            if user_input not in remaining_inputs:
                print("Invalid input. Please try again.")
        turn = O
        remaining_inputs.remove(user_input)
        return user_input
    if turn == O:
        print(O + " to move: ", end="")
        turn   = X
        round += 1
        choice = random.choice(remaining_inputs)
        remaining_inputs.remove(choice)
        return choice


def get_mark_position(position):
    global VALID_INPUTS
    return VALID_INPUTS.index(position)


## board[get_mark_position(get_input())] = turn



def game_loop():
    global X_talley, O_talley
    while True:
        global playing
        while playing:
            print_board()
            board[get_mark_position(get_input())] = turn
            if check_win() == X:
                playing = False
            if check_win() == O:
                playing = False
            if check_draw():
                playing = False
            print(CLEAR, end="")
        if check_win() == X:
            print(X + " wins!")
            X_talley += 1
            sleep(1)
        if check_win() == O:
            print(O + " wins!")
            O_talley += 1
            sleep(1)
        if check_draw():
            print("It's a draw!")
            sleep(1)
        reset_everything()

game_loop()






 
