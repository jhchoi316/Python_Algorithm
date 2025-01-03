import sys
from collections import deque
read = sys.stdin.readline

N = int(read().strip())

result = sorted(list(map(int, read().strip().split())), reverse=True)

for _ in range(N-1):
    tmp = sorted(list(map(int, read().strip().split())), reverse=True)
    
    for j in range(N):
        if tmp[j] < result[-1]:
                continue
        else:
            if tmp[j] > result[-1]:
                result[-1] = tmp[j]
                result.sort(reverse=True)

print(result[-1])