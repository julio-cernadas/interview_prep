def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def generate_board(board):
        formatted_board = []
        for i in range(n):
            row = ["Q" if col == board[i] else "." for col in range(n)]
            formatted_board.append("".join(row))
        return formatted_board

    def backtrack(board, row):
        if row == n:
            solutions.append(generate_board(board))
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    solutions = []
    board_data = [-1] * n
    backtrack(board_data, 0)
    return solutions


size = 4
output = solve_n_queens(size)
print(output)
