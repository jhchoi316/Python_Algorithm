from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(0, n+1)]
    distance = [-1]*(n+1)
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    queue = deque([1])
    distance[1] = 0
    
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1
    
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer
