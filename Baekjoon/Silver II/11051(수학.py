import sys
read = sys.stdin.readline

N, K = map(int, read().strip().split())

def factorial(N):
    tmp = 1
    for i in range(1,N+1):
        tmp *= i
    return tmp

result = factorial(N)//(factorial(K)*factorial(N-K))

print(result%10007)