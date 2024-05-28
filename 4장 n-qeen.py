global N 
N = 4
def isSafe(board, row, col): 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    return True
    if col >= N:
        return True

def solve(board, col): 
    if col >= N: 
        return True
 
    for i in range(N): 
        if isSafe(board, i, col): 
            board[i][col] = 1
            if solve(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

board = [ [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0] 
        ] 
if solve(board, 0) == False: 
     print ("정답을 찾지 못했음")
print(board) 
