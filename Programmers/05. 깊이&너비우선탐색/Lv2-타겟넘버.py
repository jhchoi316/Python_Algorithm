from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    
    while queue:
        tmp, i = queue.popleft()
        i += 1
        
        if i < len(numbers):
            queue.append([tmp+numbers[i], i])
            queue.append([tmp-numbers[i], i])
        else:
            if tmp == target:
                answer += 1
    return answer

cnt = 0

def dfs(numbers, target, current, idx):
    global cnt
    if idx == len(numbers):
        if current == target:
            cnt += 1
        return
    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt