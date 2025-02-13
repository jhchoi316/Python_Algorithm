import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
box = [list(map(int, read().split())) for _ in range(M)]
count = 0
count0 = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(M):
    count0 += box[i].count(0)
    
if count0 == 0:
    print(0)
else:
    queue = deque()
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1:
                queue.append((i,j))

    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0<=nx<M and 0<=ny<N and box[nx][ny] == 0:
                    queue.append((nx,ny))
                    box[nx][ny] = 1
        count += 1
                
    count0= 0
    for i in range(M):
        count0 += box[i].count(0)
        
    if count0 == 0:
        print(count)
    else:
        print(-1)