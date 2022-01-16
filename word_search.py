board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
m = len(board)
n = len(board[0])
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def isExist(i, row, col):
    if i == len(word):
        return True
    for direction in directions:
        newRow = row+direction[0]
        newCol = col+direction[1]
        if 0<=newRow<m and 0<=newCol<n and word[i] == board[newRow][newCol]:
            temp = board[row][col]
            board[row][col] = "0"

            if isExist(i+1, newRow, newCol):
                return True

            board[row][col] = temp
    return False
for i in range(m):
    for j in range(n):
        if board[i][j] == word[0]:
            temp = board[i][j]
            board[i][j] = "0"
            if isExist(1, i, j):
                print(True)
            board[i][j] = temp
# return False   ----needed line

