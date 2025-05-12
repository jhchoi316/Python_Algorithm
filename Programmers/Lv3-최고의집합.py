def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    quotient = s // n
    remain = s % n
    
    for i in range(n):
        answer.append(quotient)
    
    if remain != 0:
        for i in range(len(answer)):
            answer[i] += 1
            remain -= 1
            if remain == 0:
                break
    
    answer.sort()
    return answer
