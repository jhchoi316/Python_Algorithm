import sys
from collections import deque
read = sys.stdin.readline

T = int(read())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
    
for _ in range(T):
    M, N, K = map(int, read().split())
    farm = [[0]*N for _ in range(M)]
    
    for i in range(K):
        row, col = map(int, read().split())
        farm[row][col] = 1

    count = 0
    queue = deque()
    
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                queue.append((i,j))
                farm[i][j] = 0
                
                while queue:
                    a, b = queue.popleft()
                    
                    for k in range(4):
                        nx = a + dx[k]
                        ny = b + dy[k]
                        
                        if 0<=nx<M and 0<=ny<N and farm[nx][ny] == 1:
                            queue.append((nx, ny))
                            farm[nx][ny] = 0
                count += 1
    
    print(count)