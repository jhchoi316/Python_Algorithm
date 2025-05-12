from collections import deque

def bfs(begin, target, words):
    queue = deque([])
    queue.append([begin, 0])
    
    while queue:
        current, step = queue.popleft()
        
        if current == target:
            return step
        
        for w in words:
            count = 0
            for i in range(len(current)):
                if current[i] != w[i]:
                    count += 1
            if count == 1:
                queue.append([w, step+1])
            
    
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
        
    return bfs(begin, target, words)