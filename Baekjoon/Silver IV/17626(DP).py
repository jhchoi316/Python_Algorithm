import sys
import math
read = sys.stdin.readline


N = int(read())

dp = [0] * (N+1)
dp[1] = 1

for i in range(2, N+1):
    min_num = 4
    
    for j in range(1, int(math.sqrt(i))+1):
        min_num = min(min_num, dp[i-j**2])
    dp[i] = min_num +1

print(dp[N])