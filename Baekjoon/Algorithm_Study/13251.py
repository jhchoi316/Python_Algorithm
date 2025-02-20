import sys
read = sys.stdin.readline

N = int(read())
M = list(map(int, read().split()))
K = int(read())
possible = 0

def factorial(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp


n = sum(M)
total = factorial(n)//(factorial(n-K)*factorial(K))

for i in M:
    possible += factorial(i)//(factorial(i-K)*factorial(K))

            
print(possible/total)

# import sys
# import math
# read = sys.stdin.readline

# M = int(read())
# pebbles = list(map(int, read().split()))
# K = int(read())
# N = sum(pebbles)

# total = math.comb(N, K)
# possible = 0

# for p in pebbles:
#     possible += math.comb(p, K)

# print(possible/total)