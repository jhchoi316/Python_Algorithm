import sys
read = sys.stdin.readline

N = int(read())
chess = [0] * N
result = 0

def check(now):
    for i in range(now):
        if chess[now] == chess[i] or abs(chess[now]-chess[i]) == abs(now-i):
            return False
    return True

def backtracking(row):
    global result
    
    if row == N:
        result += 1
        return
    else:
        for col in range(N):
            chess[row] = col
            if check(row):
                backtracking(row+1)


backtracking(0)
print(result)