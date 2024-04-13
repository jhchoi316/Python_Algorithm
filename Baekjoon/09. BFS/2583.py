import sys



def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = []
    count = 1
    queue.append((x, y))
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<M and -1<ny<N and matrix[nx][ny]==0:
                matrix[nx][ny] = 1
                queue.append((nx, ny))
                count+=1
    return count
        
M, N, K = map(int, sys.stdin.readline().split())
matrix = [[0] * N for _ in range(M)]

for _ in range(K):
    startX, startY, endX, endY = map(int, sys.stdin.readline().split())
    
    for i in range(startY, endY):
        for j in range(startX, endX):
            matrix[i][j] = 1

res = []

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            res.append(bfs(i,j))
            
print(len(res))
print(*sorted(res))