def backtracking(cnt):
    global flag
    
    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == "X":
                    graph[i][j] = "O"
                    backtracking(cnt+1)
                    graph[i][j] = "X"

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for t in teacher:
        for k in range(4):
            nx, ny = t
            
            while 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == "O":
                    break
                if graph[nx][ny] == "S":
                    return False
            
                nx += dx[k]
                ny += dy[k]
    return True

n = int(input())

teacher = []
graph = []
flag = False

for i in range(n):
    row = list(map(str, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 'T':
            teacher.append((i, j))

backtracking(0)

if flag:
    print("YES")
else:
    print("NO")