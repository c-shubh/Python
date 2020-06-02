# Checks whether a sudoku in correct or incorrect.

'''
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
5 8 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
False

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
True

'''


def user_input():
    sudoku = []
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
            sudoku.append(inpt)
            break
    return sudoku


def check_sudoku(sudoku):
    if check_rows(sudoku) and check_cols(sudoku) and check_region(sudoku):
        return True
    else:
        return False


def check_rows(sudoku):
    for row in sudoku:
        if rows_valid(row) == False:
            return False
    return True


def rows_valid(row):
    for num in range(1, 10):
        if num not in row:
            return False
    return True


def check_cols(sudoku):
    cols = make_cols(sudoku)
    return check_rows(cols)


def make_cols(sudoku):
    cols = []
    for index in range(9):
        a = []
        for row in range(9):
            a.append(sudoku[row][index])
        cols.append(a)
        del a
    return cols


def check_region(sudoku):
    regions = make_region(sudoku)
    return check_rows(regions)


def make_region(sudoku):
    reg1 = sudoku[0][:3] + sudoku[1][:3] + sudoku[2][:3]
    reg2 = sudoku[0][3:6] + sudoku[1][3:6] + sudoku[2][3:6]
    reg3 = sudoku[0][6:] + sudoku[1][6:] + sudoku[2][6:]

    reg4 = sudoku[3][:3] + sudoku[4][:3] + sudoku[5][:3]
    reg5 = sudoku[3][3:6] + sudoku[4][3:6] + sudoku[5][3:6]
    reg6 = sudoku[3][6:] + sudoku[4][6:] + sudoku[5][6:]

    reg7 = sudoku[6][:3] + sudoku[7][:3] + sudoku[8][:3]
    reg8 = sudoku[6][3:6] + sudoku[7][3:6] + sudoku[8][3:6]
    reg9 = sudoku[6][6:] + sudoku[7][6:] + sudoku[8][6:]

    regions = []
    for reg in [reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9]:
        regions.append(reg)
    return regions


sudoku = user_input()
print(check_sudoku(sudoku))
