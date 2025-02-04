import sys
read = sys.stdin.readline

N, M = map(int, read().split())
INPUT = sorted(list(map(int, read().strip().split())))
result = []
visited = [0] * N

def dfs():
    check = 0
    
    if len(result) == M:
        print(*result)
        return
    for i in range(N):
        if check != INPUT[i] and visited[i] == 0:
            result.append(INPUT[i])
            visited[i] = 1
            check = INPUT[i]
            dfs()
            result.pop()
            visited[i] = 0
dfs()