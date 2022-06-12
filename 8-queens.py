n = int(input().strip())

board = [[0 for j in range(n+1)] for k in range(n)]

def attack(n,row,col,board):
    for j in range(1,n+1):
        if j==col:
            continue
        if board[row][j]==1:
            return True
    r,c = row-1, col+1
    while r>=0 and c<n+1:
        if board[r][c]==1:
            return True
        r-=1
        c+=1
    r,c = row+1, col+1
    while r<n and c<n+1:
        if board[r][c]==1:
            return True
        r+=1
        c+=1
    return False

def n_queens(board,n,col):
    if col==0:
        return True
    for k in range(n):
        board[k][col]=1
        if attack(n,k,col,board):
            board[k][col]=0
            continue
        if n_queens(board,n,col-1):
            return True
        else:
            board[k][col]=0
    return False

n_queens(board,n,n)

for row in board:
    print(row[1:])