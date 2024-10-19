from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    tmp = []
    
    for i in range(1, len(numbers)+1):
        tmp += list(permutations(numbers, i))
    
    num = [int(''.join(t)) for t in tmp]
    num = set(num)
    
    for i in num:
        if isPrime(i):
            answer.append(i)
            
    return len(answer)