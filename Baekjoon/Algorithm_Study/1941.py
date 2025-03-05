import sys
from collections import deque
read = sys.stdin.readline

girls = []
idx = [(i,j) for i in range(5) for j in range(5)]
result = 0
s = []
n = []

for i in range(5):
    girls.append(list(read().strip()))

def bfs(s):
    l = [i for i in s]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque([l[0]])
    l.remove(l[0])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) in l:
                queue.append((nx, ny))
                l.remove((nx, ny))
    if len(l) == 0:
        return True
    
    return False

def dfs(depth):
    global result
    if len(s) == 7:
        if n.count('S') >= 4 and bfs(s):
            result += 1
        return
    for i in range(depth, 25):
        x, y = idx[i]
        s.append((x,y))
        n.append(girls[x][y])
        dfs(i+1)
        s.pop()
        n.pop()

dfs(0)
print(result)