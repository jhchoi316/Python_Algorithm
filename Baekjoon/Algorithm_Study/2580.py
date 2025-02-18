import sys
read = sys.stdin.readline

sudoku = [list(map(int, read().split())) for _ in range(9)]
zero = []


for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i,j))
            
def rowCheck(row, num):
    for i in range(9):
        if num == sudoku[row][i]:
            return False
    return True

def colCheck(col, num):
    for i in range(9):
        if num == sudoku[i][col]:
            return False
    return True

def threeCheck(row, col, num):
    nx = row//3 * 3
    ny = col//3 * 3
    
    for i in range(3):
        for j in range(3):
            if num == sudoku[nx+i][ny+j]:
                return False
    return True


def dfs(index):
    if index == len(zero):
        for i in sudoku:
            print(*i)
        exit(0)


    for num in range(1, 10):
        # 0이 있는 좌표
        x = zero[index][0]
        y = zero[index][1]
        
        if rowCheck(x, num) and colCheck(y, num) and threeCheck(x, y, num):
            sudoku[x][y] = num
            dfs(index+1)
            sudoku[x][y] = 0

dfs(0)