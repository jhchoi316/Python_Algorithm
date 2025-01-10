import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
A = list(map(int, read().strip().split()))
B = list(map(int, read().strip().split()))
M = int(read())
C = list(map(int, read().strip().split()))

result = deque()

for i in range(N):
    if A[i] == 0:
        result.appendleft(B[i])

for i in range(M):
    result.append(C[i])
    print(result.popleft(), end = ' ')