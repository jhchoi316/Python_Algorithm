t = int(input())
dp = [[0]*30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

for i in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])