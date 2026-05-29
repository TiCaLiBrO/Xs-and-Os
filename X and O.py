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

WIN_TIMER      = 0.5
MOVE_TIMER     = 0.2
SPECTATE_TIMER = 0.1
## Add a spectating win timer
## Rename Spectate timer to spectate_move_timer.

VALID_INPUTS = ["top left", "top", "top right", "left", "middle", "right", "bottom left", "bottom", "bottom right"]
remaining_inputs = ["top left", "top", "top right", "left", "middle", "right", "bottom left", "bottom", "bottom right"]

print(YELLOW + "Modes involding the learning AI and optimal AI are not implemented yet." + WHITE)



last_player1 = O
turn         = X
round        = 1
playing      = True
game_counter = 1

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

X_talley = 0
O_talley = 0

"┃"
"┃┃"
"┃┃┃"
"┃┃┃┃"
"╋╋╋╋"


game_mode = None

def start_menu():
    juno = None
    while juno != "1" or juno != "2" or juno != "3":
        print("Enter a number to select a mode:")
        print("1 -> Player Versus AI")
        print("2 -> Player Versus Player")
        print("3 -> Spectate AI Versus AI")
        juno = input()
        if juno == "1":
            print("Enter a number to select a mode:")
            print("1 -> Player versus Weak AI")
            print("2 -> Player versus Learning AI")
            print("3 -> Player versus Optimal AI")
            while juno != "1" or juno != "2" or juno != "3":
                juno = input()
                if juno == "1":
                    return "Player versus Weak AI"
                elif juno == "2":
                    return "Player versus Learning AI"
                elif juno == "3":
                    return "Player versus Optimal AI"
                else:
                    print("Invalid input. Try again.")
                    juno = None
        elif juno == "2":
            return "Player versus Player"
        elif juno == "3":
            print("Enter a number to select a mode:")
            print("1 -> Spectate Weak AI versus Weak AI")
            print("2 -> Spectate Weak AI versus Learning AI")
            print("3 -> Spectate Weak AI versus Optimal AI")
            print("4 -> Spectate Learning AI versus Learning AI")
            print("5 -> Spectate Learning AI versus Optimal AI")
            print("6 -> Spectate Optimal AI versus Optimal AI")
            while juno != "1" or juno != "2" or juno != "3" or juno != "4" or juno != "5" or juno != "6":
                juno = input()
                if juno == "1":
                    return "Weak AI verusus Weak AI"
                elif juno == "2":
                    return "Weak AI versus Learning AI"
                elif juno == "3":
                    return "Weak AI versus Optimal AI"
                elif juno == "4":
                    return "Learning AI versus Learning AI"
                elif juno == "5":
                    return "Learning AI versus Optimal AI"
                elif juno == "6":
                    return "Optimal AI versus Optimal AI"
                else:
                    print("Invalid input. Try again.")
                    juno = None
        else:
            print("Invalid input. Try again.")
            juno = None

game_mode = start_menu()
print(CLEAR, end="")


# we now have 10 game modes. 
#  1 Working
#  2 --- Need Learning AI
#  3 --- Need Optimal AI
#  4 Workable
#  5 Workable
#  6 --- Need Learning AI
#  7 --- Need Optimal AI
#  8 --- Need Learning AI
#  9 --- Need Learning AI & Optimal AI
# 10 --- Need Optimal AI






print(YELLOW + "The following are the valid inputs for placing your " + X + YELLOW + " or " + O + YELLOW + " on the board:")
print(YELLOW + "top left, top, top right, left, middle, right, bottom left, bottom, bottom right" + WHITE)



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
    print("game:  " + str(game_counter))
    print("round: " + str(round))
    print(board[0] + " ┃ " + board[1] + " ┃ " + board[2])
    print("━━╋━━━╋━━", end=""); print_X_talley()
    print(board[3] + " ┃ " + board[4] + " ┃ " + board[5])
    print("━━╋━━━╋━━", end=""); print_O_talley()
    print(board[6] + " ┃ " + board[7] + " ┃ " + board[8])



def get_player_versus_weak_ai_input():
    global last_player1, turn, round, remaining_inputs, MOVE_TIMER, VALID_INPUTS
    user_input = None
    if turn == X:
        while user_input not in remaining_inputs:
            user_input = input(X + " to move: ")
            if user_input not in remaining_inputs:
                print("Invalid input. Please try again.")
        turn = O
        if last_player1 == O:
            round += 1
        remaining_inputs.remove(user_input)
        return user_input
    if turn == O:
        print(O + " to move: ", end="")
        sleep(MOVE_TIMER)
        turn   = X
        if last_player1 == X:
            round += 1
        choice = random.choice(remaining_inputs)
        remaining_inputs.remove(choice)
        return choice

def player_versus_weak_ai_game_loop():
    global X_talley, O_talley, game_counter, WIN_TIMER, playing, turn
    while True:
        while playing:
            print_board()
            board[get_mark_position(get_player_versus_weak_ai_input())] = turn
            if check_win() == X:
                playing = False
            if check_win() == O:
                playing = False
            if check_draw():
                playing = False
            print(CLEAR, end="")
        if check_win() == X:
            print(X + " wins!")
            game_counter += 1
            X_talley     += 1
            sleep(WIN_TIMER)
        if check_win() == O:
            print(O + " wins!")
            game_counter += 1
            O_talley     += 1
            sleep(WIN_TIMER)
        if check_draw():
            print("It's a draw!")
            game_counter += 1
            sleep(WIN_TIMER)
        reset_everything()



def get_player_versus_player_input():
    global last_player1, turn, round, remaining_inputs, MOVE_TIMER, VALID_INPUTS
    user_input = None
    if turn == X:
        while user_input not in remaining_inputs:
            user_input = input(X + " to move: ")
            if user_input not in remaining_inputs:
                print("Invalid input. Please try again.")
        turn = O
        if last_player1 == O:
            round += 1
        remaining_inputs.remove(user_input)
        return user_input
    if turn == O:
        while user_input not in remaining_inputs:
            user_input = input(O + " to move: ")
            if user_input not in remaining_inputs:
                print("Invalid input. Please try again.")
        turn = X
        if last_player1 == X:
            round += 1
        remaining_inputs.remove(user_input)
        return user_input

def player_versus_player_game_loop():
    global X_talley, O_talley, game_counter, WIN_TIMER, playing, turn
    while True:
        while playing:
            print_board()
            board[get_mark_position(get_player_versus_player_input())] = turn
            if check_win() == X:
                playing = False
            if check_win() == O:
                playing = False
            if check_draw():
                playing = False
            print(CLEAR, end="")
        if check_win() == X:
            print(X + " wins!")
            game_counter += 1
            X_talley     += 1
            sleep(WIN_TIMER)
        if check_win() == O:
            print(O + " wins!")
            game_counter += 1
            O_talley     += 1
            sleep(WIN_TIMER)
        if check_draw():
            print("It's a draw!")
            game_counter += 1
            sleep(WIN_TIMER)
        reset_everything()




def get_weak_ai_versus_weak_ai_input():
    global last_player1, turn, round, remaining_inputs, SPECTATE_TIMER, VALID_INPUTS
    user_input = None
    if turn == X:
        print(X + " to move: ", end="")
        sleep(SPECTATE_TIMER)
        turn   = O
        if last_player1 == O:
            round += 1
        choice = random.choice(remaining_inputs)
        remaining_inputs.remove(choice)
        return choice
    if turn == O:
        print(O + " to move: ", end="")
        sleep(SPECTATE_TIMER)
        turn   = X
        if last_player1 == X:
            round += 1
        choice = random.choice(remaining_inputs)
        remaining_inputs.remove(choice)
        return choice

def weak_ai_versus_weak_ai_game_loop():
    global X_talley, O_talley, game_counter, WIN_TIMER, playing, turn
    while True:
        while playing:
            print_board()
            board[get_mark_position(get_weak_ai_versus_weak_ai_input())] = turn
            if check_win() == X:
                playing = False
            if check_win() == O:
                playing = False
            if check_draw():
                playing = False
            print(CLEAR, end="")
        if check_win() == X:
            print(X + " wins!")
            game_counter += 1
            X_talley     += 1
            sleep(WIN_TIMER)
        if check_win() == O:
            print(O + " wins!")
            game_counter += 1
            O_talley     += 1
            sleep(WIN_TIMER)
        if check_draw():
            print("It's a draw!")
            game_counter += 1
            sleep(WIN_TIMER)
        reset_everything()






def get_mark_position(position):
    global VALID_INPUTS
    return VALID_INPUTS.index(position)


## board[get_mark_position(get_input())] = turn











get_input = None


def choose_game_mode():
    global game_mode, get_input
    if game_mode == "Player versus Weak AI":
        player_versus_weak_ai_game_loop()
    if game_mode == "Player versus Learning AI":
        print("Not Implemented Yet.")
    if game_mode == "Player versus Optimal AI":
        print("Not Implemented Yet.")
    if game_mode == "Player versus Player":
        player_versus_player_game_loop()
    if game_mode == "Weak AI verusus Weak AI":
        weak_ai_versus_weak_ai_game_loop()
    if game_mode == "Weak AI versus Learning AI":
        print("Not Implemented Yet.")
    if game_mode == "Weak AI versus Optimal AI":
        print("Not Implemented Yet.")
    if game_mode == "Learning AI versus Learning AI":
        print("Not Implemented Yet.")
    if game_mode == "Learning AI versus Optimal AI":
        print("Not Implemented Yet.")
    if game_mode == "Optimal AI versus Optimal AI":
        print("Not Implemented Yet.")

choose_game_mode()


#
"""
def game_loop():
    global X_talley, O_talley, game_counter, WIN_TIMER, playing, get_input
    while True:
        while playing:
            print_board()
            board[get_mark_position(get_input)] = turn
            if check_win() == X:
                playing = False
            if check_win() == O:
                playing = False
            if check_draw():
                playing = False
            print(CLEAR, end="")
        if check_win() == X:
            print(X + " wins!")
            game_counter += 1
            X_talley     += 1
            sleep(WIN_TIMER)
        if check_win() == O:
            print(O + " wins!")
            game_counter += 1
            O_talley     += 1
            sleep(WIN_TIMER)
        if check_draw():
            print("It's a draw!")
            game_counter += 1
            sleep(WIN_TIMER)
        reset_everything()
"""



# TO DO:
#   - Make a learning AI
#   - Make an optimal AI
#   - Add spectating mode
#   - Add an option to play against learning AI
#   - Add an option to play against Optimal AI


 
# New issue found. A rare bug where you cannot place a piece where you want (maybe I'm just insane though. It's super rare)