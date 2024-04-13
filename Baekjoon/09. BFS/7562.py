import sys

t = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs():
    queue = []
    queue.append((startX,startY))
    
    while queue:
        x, y = queue.pop(0)
        if x == endX and y == endY:
            return matrix[x][y] - 1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if -1<nx<i and -1<ny<i and matrix[nx][ny]==0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))
            

for j in range(t):
    i = int(input())
    startX, startY = map(int, sys.stdin.readline().split())
    endX, endY = map(int, sys.stdin.readline().split())
    
    matrix = [[0] * i for _ in range(i)]
    matrix[startX][startY] = 1
    print(bfs())
    