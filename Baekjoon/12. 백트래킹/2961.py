import sys

def dfs(start, visited, s, b):
    global SB_min
    
    if b != 0:
        SB_min = min(SB_min, abs(s-b))
    
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(start+1, visited, s*taste[i][0], b+taste[i][1])
            visited[i] = False

n = int(input())
SB_min = sys.maxsize

taste = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

dfs(0, visited, 1, 0)
print(SB_min)