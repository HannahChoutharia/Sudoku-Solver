board = []

print("WELCOME TO SUDOKU SOLVER!")
print("Enter the Sudoku row by row.")
print("Use 0 for empty cells.")

for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    while len(row) != 9:
        print("Please enter exactly 9 numbers.")
        row = list(map(int, input(f"Row {i+1}: ").split()))
    board.append(row)

import copy
original_board = copy.deepcopy(board)


def print_board(board):
    for row in range(len(board)):
        if row != 0 and row % 3 == 0:
            print("-" * 21)

        for col in range(len(board[row])):
            if col != 0 and col % 3 == 0:
                print("|", end=" ")

            print(board[row][col], end=" ")

        print()


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, row, col, num):

    # Check row
    for c in range(9):
        if board[row][c] == num and c != col:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == num and r != row:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_column = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_column, start_column + 3):
            if board[r][c] == num and (r, c) != (row, col):
                return False

    return True


def solve(board):
    position = find_empty(board)

    if position is None:
        return True

    row, col = position

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


print("\nOriginal Sudoku:\n")
print_board(original_board)

print("\nSolving...\n")

if solve(board):
    print("Solved Sudoku:\n")
    print_board(board)
else:
    print("No solution exists.")
