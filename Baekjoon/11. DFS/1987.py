import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

r, c = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(r)]
check = set()
ans = 0

def dfs(x, y, count):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    global ans
    ans = max(ans, count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<r and 0<=ny<c and not graph[nx][ny] in check:
            check.add(graph[nx][ny])
            dfs(nx, ny, count+1)
            check.remove(graph[nx][ny])

check.add(graph[0][0])
dfs(0,0,1)
print(ans)
