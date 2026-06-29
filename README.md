# Sudoku Solver (Python)

A Python-based Sudoku Solver that solves any valid 9×9 Sudoku puzzle using the **Backtracking Algorithm**.

## Features

* Solves any valid Sudoku puzzle.
* Takes input from the user row by row.
* Validates the input size.
* Displays the original Sudoku.
* Prints the solved Sudoku.
* Uses recursive backtracking for efficient solving.

## Technologies Used

* Python 3

## How to Run

1. Clone this repository.
2. Open the project in your preferred Python IDE (VS Code, PyCharm, etc.).
3. Run the Python file.
4. Enter the Sudoku row by row using spaces between numbers.
5. Use `0` for empty cells.

### Example Input

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

## Algorithm

This project uses the **Backtracking Algorithm**, which:

* Finds an empty cell.
* Tries numbers from 1 to 9.
* Checks whether the number is valid.
* Recursively continues until the puzzle is solved.
* Backtracks if no valid number can be placed.

## Future Improvements

* GUI version using Tkinter or PyQt.
* Read Sudoku from a file.
* Generate random Sudoku puzzles.
* Add difficulty levels.

## Author

Hannah Choutharia
