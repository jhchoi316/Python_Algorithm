import sys
from itertools import combinations
read = sys.stdin.readline

N, M = map(int, read().split())
INPUT = sorted(set(list(map(int, read().split()))))
result = []

def backTracking(count, index):
    if count == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(index, len(INPUT)):
        result.append(INPUT[i])
        backTracking(count+1, i)
        result.pop()
        

backTracking(0,0)
