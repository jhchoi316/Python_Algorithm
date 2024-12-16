import sys
from itertools import combinations
read = sys.stdin.readline

n, m, k = map(int, read().split())

ans = 0
all = [*combinations([i for i in range(n)], m)]

for i in all:
    cnt = 0
    for j in range(m):
        if i[j] < m:
            cnt+=1
    if cnt >= k: 
        ans += 1

print(ans / len(all))