import sys
read = sys.stdin.readline

def dfs(start, now, cost, count):
    global result
    
    if count == n:
        if weights[now][start]:
            cost += weights[now][start]
            if result > cost:
                result = cost
        return

    if cost > result:
        return
    
    for i in range(n):
        if not visited[i] and weights[now][i]:
            visited[i] = True
            dfs(start, i, cost + weights[now][i], count+1)
            visited[i] = False
    
n = int(read())
weights = [list(map(int, read().split())) for _ in range(n)]
visited = [False] * n
result = sys.maxsize

for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = 0
    
print(result)