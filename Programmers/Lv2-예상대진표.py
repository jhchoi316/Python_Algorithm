def solution(n,a,b):
    answer = 0
    
    while a!=b:
        if a%2 == 0:
            a //= 2
        else:
            a //= 2
            a += 1
            
        if b%2 == 0:
            b //= 2
        else:
            b //= 2
            b += 1
        answer += 1
    return answer