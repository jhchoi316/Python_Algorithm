import sys
read = sys.stdin.readline

N = int(read().strip())
A = list(map(int, read().strip().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))