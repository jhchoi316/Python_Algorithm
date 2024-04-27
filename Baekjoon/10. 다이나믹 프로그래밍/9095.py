# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 7
# 5 -> 13
# 6 -> 24
# 7 -> 44 

T = int(input())

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in range(T):
    print(dp[int(input())])
