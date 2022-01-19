board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
def checkValid(row, col, num):
    for i in range(9):
        if board[row][i] == str(num):
            return False
    for j in range(9):
        if board[j][col] == str(num):
            return False
    boxRow = row // 3
    boxCol = col // 3
    for i in range(3*boxRow, 3*boxRow + 3):
        for j in range(3*boxCol, 3*boxCol + 3):
            if board[i][j] == str(num):
                return False
    return True
def solve(row, col):
    while board[row][col] != ".":
        col += 1
        if col == 9:
            col = 0
            row += 1
        if row == 9:
            return True
    for i in range(1, 10):
        if checkValid(row, col, i):
            board[row][col] = str(i)
            if solve(row, col):
                return True
            board[row][col] = "."
    return False
solve(0, 0) 
print(board)