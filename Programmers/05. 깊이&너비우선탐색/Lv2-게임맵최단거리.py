from collections import deque

def bfs(maps, start, end):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([start, end])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1<nx<len(maps) and -1<ny<len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx,ny])

    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = 0
    
    answer = bfs(maps,0,0)
    
    return -1 if answer == 1 else answer