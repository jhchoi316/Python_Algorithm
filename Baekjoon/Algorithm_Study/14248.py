import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))
S = int(read())
visited = [False]*N
count = 1

def dfs(x):
    global count
    # 오른쪽, 왼쪽
    for nx in [x+A[x], x-A[x]]:
        if 0<=nx<N and not visited[nx]:
            count += 1
            visited[nx] = True
            dfs(nx)
        
dfs(S-1)
print(count)