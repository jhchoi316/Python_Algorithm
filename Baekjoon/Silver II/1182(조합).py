import sys
from itertools import combinations
read = sys.stdin.readline

N, S = map(int, read().split())
INPUT = list(map(int, read().split()))
result = 0

for i in range(1, N+1):
    for x in combinations(INPUT, i):
        if sum(x) == S:
            result += 1

print(result)