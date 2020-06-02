'''Solves a sudoku.'''
# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]


def user_input():
    board = []
    for i in range(9):
        while True:
            inpt = list(map(int, input().split()))
            if len(inpt) != 9:
                print("Invalid input")
                continue
            for i in inpt:
                if 1 < i > 9:
                    print("Invalid input")
                    continue
            board.append(inpt)
            break
    return board


def print_board(board):
    '''Prints the board.'''
    for x in range(9):
        if x != 0 and x % 3 == 0:
            print(" ──────┼───────┼──────")
        for y in range(9):
            if y != 0 and y % 3 == 0:
                print("│ ", end='')
            if y == 0:
                print(' ', end='')
            print(str(board[x][y]) + ' ', end='')
        print()


def solve(board):
    '''The main backtracking algorithm.'''
    find = find_empty(board)
    if find is None:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def valid(board, num, pos):
    '''
    Checks if a given number is valid to be at a given empty cell.
    Checks the row, column and the 3x3 square for the number to be valid or invalid.
    Returns True if valid and False if invalid
    '''
    x, y = pos[0], pos[1]
    # Check row
    for i in range(9):
        if num == board[x][i] and i != y:
            return False
    # Check column
    for i in range(9):
        if num == board[i][y] and i != x:
            return False
    # Check 3x3 square
    square_x, square_y = x//3, y//3
    for i in range(square_x*3, square_x*3+3):
        for j in range(square_y*3, square_y*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    # If none of the above are satisfied
    return True


def find_empty(board):
    '''Finds an empty cell in the board.'''
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return (x, y)
    return None


board = user_input()
print_board(board)
print()
solve(board)
print()
print_board(board)

# 9 0 0 7 1 0 0 8 0
# 5 0 8 0 4 9 0 0 7
# 0 0 2 0 6 0 0 0 9
# 2 8 1 0 0 0 9 6 0
# 0 0 0 0 9 1 8 0 4
# 4 0 0 6 0 0 0 0 0
# 3 0 0 9 8 7 0 0 1
# 0 1 6 4 0 0 2 0 8
# 0 9 4 1 2 6 3 0 5
