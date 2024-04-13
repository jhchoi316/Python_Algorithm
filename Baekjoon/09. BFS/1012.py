import sys

t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = [(x, y)]
    graph[x][y] = 0
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            mx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < mx < m and -1 < ny < n and graph[mx][ny] == 1:
                queue.append((mx,  ny))
                graph[mx][ny] = 0

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*n for _ in range(m)]
    count = 0
    
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
        
    for a in range(m):
        for b in range(n):
            if graph[a][b]==1:
                bfs(a,b)
                count += 1

    print(count) 