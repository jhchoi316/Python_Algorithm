import sys
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().strip().split()))

dp = [1] * N

for i in range( N):
    for j in range(i):
        if INPUT[i] > INPUT[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))