def exist(board, word) -> bool:
    def dfs(row, col, i):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]:
            return False
        if i == len(word) - 1:
            return True

        temp, board[row][col] = board[row][col], "#"
        x = dfs(row + 1, col, i + 1)
        y = dfs(row - 1, col, i + 1)
        z = dfs(row, col + 1, i + 1)
        d = dfs(row, col - 1, i + 1)
        board[row][col] = temp

        return any([x, y, z, d])

    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True

    return False


data = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
target = "ABCCED"
output = exist(data, target)
print(output)
