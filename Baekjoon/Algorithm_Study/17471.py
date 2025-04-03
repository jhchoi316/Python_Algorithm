import sys
from itertools import combinations
from collections import deque
read = sys.stdin.readline

N = int(read())
population = [0] + list(map(int, read().split()))
region = [[] for _ in range(N+1)]

for i in range(1, N+1):
    INPUT = list(map(int, read().split()))
    INPUT = INPUT[1:]
    
    for j in INPUT:
        region[i].append(j)

# 가능한 구역 나누기
def get_combinations(lists):
    tmp = []
    for i in range(1, N+1):
        for j in combinations(lists, i):
            tmp.append((j, tuple(set(lists) - set(j))))
    return tmp

def bfs(area):
    if area:
        start = area[0]
    else:
        return 0, 0

    queue = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1
    visit_count, cost = 1, 0
    
    while queue:
        v = queue.popleft()
        cost += population[v]
        
        for i in region[v]:
            if not visited[i] and i in area:
                visited[i] = 1
                visit_count += 1
                queue.append(i)
    return visit_count, cost

result = 1e9

for i in get_combinations([i for i in range(1, N+1)]):
    visit_count1, cost1 = bfs(i[0])
    visit_count2, cost2 = bfs(i[1])
    
    if visit_count1 + visit_count2 == N:
        result = min(result, abs(cost1 - cost2))

print(-1 if result == 1e9 else result)