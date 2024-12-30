import sys
from itertools import permutations
read = sys.stdin.readline

N = [i for i in range(1,int(read().strip())+1)]
result = []

for i in list(permutations(N, len(N))):
    result.append(i)

result.sort()

for i in result:
    print(' '.join(map(str, i)))