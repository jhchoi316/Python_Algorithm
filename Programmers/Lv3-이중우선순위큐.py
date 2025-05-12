from collections import deque

def solution(operations):
    answer = deque([])
    
    for i in operations:
        op, value = map(str, i.strip().split())
        
        if op == "I":
            answer.append(int(value))
            answer = deque(sorted(answer))
            
        elif op == "D" and value == "1":
            if not answer:
                continue
            else:
                answer.pop()
                    
        elif op == "D" and value == "-1":
            if not answer:
                continue
            else:
                answer.popleft()                
    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0, 0]