N = int(input())
p1, p2 = map(int, input().split())

family = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

for _ in range(int(input())):
    x, y = map(int, input().split())  
    family[x].append(y)
    family[y].append(x)

# dfs
def dfs(v, num):
    num += 1
    visited[v] = True

    if v == p2:
        print(num-1)
        exit(0)

    for i in family[v]:
        if not visited[i]:
            dfs(i, num)

dfs(p1, 0)

print(-1)