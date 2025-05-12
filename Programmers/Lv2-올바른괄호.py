def solution(s):
    answer = True
    s = list(s.strip())
    result = []

    while s:
        index = s.pop()
        if index == ')':
            result.append(index)
        else:
            if result:
                result.pop()
            else:
                answer = False
                break
    if result:
        answer = False
        
    return answer