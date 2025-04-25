from collections import deque
    
def solution(n, edge):
    answer = 0
    vertex = [[] for _ in range(n+1)]
    visited = [0] *(n+1)
    
    for i in edge:
        vertex[i[0]].append(i[1])
        vertex[i[1]].append(i[0])
    
    queue = deque() 
    queue.append(1)
    visited[1] = 1 
    
    while queue:
        x = queue.popleft() 
        for i in vertex[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1 
                queue.append(i)
    
    max_value = max(visited)
    answer = visited.count(max_value)
    
    return answer