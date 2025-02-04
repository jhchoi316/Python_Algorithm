import sys
from itertools import permutations
read = sys.stdin.readline

N, M = map(int, read().split())
INPUT = list(map(int, read().strip().split()))
result = set()

for i in permutations(INPUT, M):
    result.add(i)

result = sorted(list(result))

for i in result:
    print(*i)