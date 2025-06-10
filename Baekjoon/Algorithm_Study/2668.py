import sys
read = sys.stdin.readline

# 첫쨰줄: 1~N 차례대로
# 둘쨰줄: 1~N 정수

# 첫쨰줄에서 뽑으면 -> 그 정주들이 이루는 집합 == 둘째줄에 들어 있는 집합

# now: 현재 좌표, start: 시작 좌표
def dfs(now, start):
    visited[now] = True
    # 다음 값
    next = graph[now]

    # 현재 값을 방문하지 않았다면, dfs
    if not visited[next]:
        dfs(next, start)
    # 현재 값을 방문했고, 사이클이 있는지 확인 
    elif visited[next] and next == start:
        answer.append(next)
        
N = int(read())
# 1부터 시작
graph = [0]+[int(read()) for i in range(N)]
answer = []

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)

print(len(answer))

for i in answer:
    print(i)