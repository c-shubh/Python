# tic-tac-toe
from tabulate import tabulate
import os
from random import randint


def clear():
    # clears the console
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")


def board_print(b):
    # prints the tic-tac-toe board
    table = [[b[0], b[1], b[2]], [b[3], b[4], b[5]], [b[6], b[7], b[8]]]
    print(tabulate(table, tablefmt='fancy_grid'))


def player1_turn(b):
    # handles the input of player1
    global player1
    while True:
        try:
            loc = int(input(f"{player1}'s turn. Enter location: "))
        except KeyboardInterrupt:
            raise
        except:
            print("Invalid input.")
            continue
        try:
            if b[loc - 1] != 'O':
                b[loc - 1] = 'X'
                break
            else:
                print("Invalid move.")
        except KeyboardInterrupt:
            raise
        except:
            print("Invalid move.")


def player2_turn(b):
    # handles the input of player2
    global player2
    while True:
        try:
            loc = int(input(f"{player2}'s turn. Enter location: "))
        except KeyboardInterrupt:
            raise
        except:
            print("Invalid input.")
            continue
        try:
            if b[loc - 1] != 'X':
                b[loc - 1] = 'O'
                break
            else:
                print("Invalid move.")
        except KeyboardInterrupt:
            raise
        except:
            print("Invalid move.")


def check_rows(b):
    # checks the rows for triads of X or O
    row1 = [b[0], b[1], b[2]]
    row2 = [b[3], b[4], b[5]]
    row3 = [b[6], b[7], b[8]]
    if '' not in row1 and len(set(row1)) == 1:
        return row1[0] + '_wins'
    elif '' not in row2 and len(set(row2)) == 1:
        return row2[0] + '_wins'
    elif '' not in row3 and len(set(row3)) == 1:
        return row3[0] + '_wins'


def check_cols(b):
    # checks the columns for triads of X or O
    col1 = [b[0], b[3], b[6]]
    col2 = [b[1], b[4], b[7]]
    col3 = [b[2], b[5], b[8]]
    if '' not in col1 and len(set(col1)) == 1:
        return col1[0] + '_wins'
    elif '' not in col2 and len(set(col2)) == 1:
        return col2[0] + '_wins'
    elif '' not in col3 and len(set(col3)) == 1:
        return col3[0] + '_wins'


def check_diags(b):
    # checks the diagonals for triads of X or O
    diag1 = [b[0], b[4], b[8]]
    diag2 = [b[2], b[4], b[6]]
    if '' not in diag1 and len(set(diag1)) == 1:
        return diag1[0] + '_wins'
    elif '' not in diag2 and len(set(diag2)) == 1:
        return diag2[0] + '_wins'


def check(b):
    # finalises the winner or draw
    if any(retnd_val == 'X_wins' for retnd_val in [check_rows(b), check_cols(b), check_diags(b)]):
        return 'X_wins'
    elif any(retnd_val == 'O_wins' for retnd_val in [check_rows(b), check_cols(b), check_diags(b)]):
        return 'O_wins'
    else:
        for ans in b:
            if ans not in ['X', 'O']:
                return 'not_draw'
        return 'draw'


def game_mode1():
    # controls the game mode 1
    global player1
    global player2

    # main
    while True:
        clear()
        board_print(b)
        player1_turn(b)
        clear()
        board_print(b)
        if check(b) == 'X_wins':
            print(f'{player1} wins.')
            break
        if check(b) == 'draw':
            print('Draw.')
            break
        player2_turn(b)
        clear()
        board_print(b)
        if check(b) == 'O_wins':
            print(f'{player2} wins.')
            break
        if check(b) == 'draw':
            print('Draw.')
            break


def computer_turn(b):
    while True:
        rand = randint(0, 8)
        if b[rand] == '':
            b[rand] = 'X'
            break


def game_mode2():
    # controls the game mode 2

    # main
    while True:
        clear()
        board_print(b)
        computer_turn(b)
        clear()
        board_print(b)
        if check(b) == 'X_wins':
            print('Computer wins.')
            break
        if check(b) == 'draw':
            print('Draw.')
            break
        player2_turn(b)
        clear()
        board_print(b)
        if check(b) == 'O_wins':
            print(f'{player2} wins.')
            break
        if check(b) == 'draw':
            print('Draw.')
            break


b = ['', '', '', '', '', '', '', '', '']  # tic-tac-toe board
opt = [1, 2]

while True:
    try:
        game_mode = opt[int(
            input("Select game mode:\n1. Human vs Human\n2. Computer vs Human\n"))-1]
        print()
        break
    except:
        print("Invalid input.")
        print()

if game_mode == 1:
    player1 = input('Enter player1 (X): ')
    player2 = input('Enter player2 (O): ')
    game_mode1()
else:
    player2 = input("Enter your name: ")
    game_mode2()
