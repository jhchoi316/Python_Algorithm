import sys
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().strip().split()))

dp = [1]*N
dp[0] = INPUT[0]

for i in range(1, N):
    for j in range(i):
        if INPUT[j]<INPUT[i]:
            dp[i] = max(dp[i], dp[j]+INPUT[i])
        else:
            dp[i] = max(dp[i], INPUT[i])

print(max(dp))