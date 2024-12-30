import sys
from itertools import permutations
read = sys.stdin.readline

N = int(read().strip())
result = []

def dfs():
    if len(result) == N:
        print(*result)
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()