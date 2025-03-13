def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    """Check if a queen can be safely placed at the given position."""
    # Check column safety
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal safety
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal safety
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    # Check if the board is full -> solution found
    if row == len(board):
        return True

    # Try placing a queen in each column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):  # Recursively solve the next row
                return True
            board[row][col] = 0  # Backtrack

    return False

def get_solution():
    """Solves the eight queens algorithm and returns the solution as a list 
    of queen positions. Each queen is represented as a dict with 'row' and 'col'."""
    n = 8
    board = [[0] * n for _ in range(n)]
    if solve_n_queens(board, 0):
        queens = []
        for row in range(n):
            for col in range(n):
                if board[row][col] == 1:
                    queens.append({"row": row, "col": col})
        return queens
    return None

def get_queens_from_board(board):
    n = len(board)
    queens = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                queens.append({"row": row, "col": col})
    return queens

def solve_n_queens_steps(board, row, steps):
    # Record current board state
    steps.append(get_queens_from_board(board))
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            steps.append(get_queens_from_board(board))
            if solve_n_queens_steps(board, row + 1, steps):
                return True
            board[row][col] = 0
            steps.append(get_queens_from_board(board))
    return False

def get_solution_steps():
    n = 8
    board = [[0] * n for _ in range(n)]
    steps = []
    solve_n_queens_steps(board, 0, steps)
    return steps

if __name__ == "__main__":
    steps = get_solution_steps()
    print("Steps:")
    for step in steps:
        print(step)