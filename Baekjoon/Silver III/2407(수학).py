import sys
read = sys.stdin.readline

N, M = map(int, read().strip().split())

def factorial(N):
    num = 1
    for i in range(2, N+1):
        num *= i
    return num

print(factorial(N)//((factorial(M))*factorial(N-M)))