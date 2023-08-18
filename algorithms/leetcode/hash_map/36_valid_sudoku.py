from collections import defaultdict


def is_valid_sukoku(board) -> bool:
    cols = defaultdict(list)
    rows = defaultdict(list)
    squares = defaultdict(list)

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == ".":
                continue

            if (
                board[row][col] in rows[row]
                or board[row][col] in cols[col]
                or board[row][col] in squares[(row // 3, col // 3)]
            ):
                return False

            cols[col].append(board[row][col])
            rows[row].append(board[row][col])
            squares[(row // 3, col // 3)].append(board[row][col])

    return True


data = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
output = is_valid_sukoku(data)
print(output)
