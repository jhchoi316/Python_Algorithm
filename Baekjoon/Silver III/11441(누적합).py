import sys
read = sys.stdin.readline

N = int(read().strip())
A = list(map(int, read().strip().split()))
M = int(read().strip())

result = [0 for _ in range(N+1)]
result[1] = A[0]

for i in range(2, N+1):
    result[i] = result[i-1] + A[i-1]

for _ in range(M):
    i, j = map(int, read().strip().split())

    if i == 1:
        print(result[j])
    else:
        print(result[j]-result[i-1])