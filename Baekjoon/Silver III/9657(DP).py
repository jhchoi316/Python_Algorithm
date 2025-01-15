import sys
read = sys.stdin.readline

N = int(read().strip())

dp = [0] * 1001
dp[1], dp[2], dp[3], dp[4] = 1, 0, 1, 1
stones = [1, 3, 4]

for i in range(5, N+1):
    for s in stones:
        if dp[i-s] == 0:
            dp[i] = 1
            break
        
        dp[i] = 0

if dp[N] == 0:
    print("CY")
else:
    print("SK")