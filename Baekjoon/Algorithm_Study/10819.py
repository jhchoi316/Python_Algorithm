import sys
from itertools import permutations
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().split()))
result = 0

for i in permutations(INPUT):
    tmp = 0
    for j in range(N-1):
        tmp += abs(i[j]-i[j+1])
    
    if tmp > result:
        result = tmp

print(result)