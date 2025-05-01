from collections import deque

def solution(n, wires):
    answer = []
    remove = 0
    
    while remove != len(wires):
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        count = 1
        for idx, w in enumerate(wires):
            if idx != remove:
                graph[w[0]].append(w[1])
                graph[w[1]].append(w[0])

        queue = deque([1])
        visited[1] = True
        
        while queue:
            x = queue.popleft()
            
            for i in graph[x]:
                if not visited[i]:
                    count += 1
                    queue.append(i)
                    visited[i] = True
        
        answer.append(abs(n-count-count))
        remove += 1

    return min(answer)