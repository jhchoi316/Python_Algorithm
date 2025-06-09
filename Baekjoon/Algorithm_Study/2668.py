import sys
read = sys.stdin.readline

answer = set()
N = int(read())
graph = [[i,int(read())] for i in range(1,N+1)]
visited = [False] * (N+1)

def dfs(start):
    if visited[start][0]
    dfs(graph[i])
    
for i in range(1, N+1):
    if graph[i][0] == graph[i][1]:
        answer.append(i)
        visited[i] = True
    if not visited[i]:
        visited[i] = True
        dfs(i)
        visited[i] = False

print(len(answer))
for i in list(answer).sort():
    print(i)