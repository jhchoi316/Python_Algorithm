def solution(s):
    answer = True
    l = list(s)
    tmp = []
    
    for i in range(len(l)):
        # tmp가 비어있고 # '('일 때
        if l[i] == '(':
            tmp.append(l[i])
            
        # tmp가 비어있고 # '('일 때
        elif not tmp and l[i] == ')':
            answer = False
            break
        # tmp가 차있고 # ')'일 때
        elif tmp and l[i] == ')':
            tmp.pop()
            
    if tmp:
        answer = False
    
    return answer