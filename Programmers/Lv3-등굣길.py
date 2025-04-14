def solution(m, n, puddles):
    puddles = [[x,y] for [y,x] in puddles]
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: 
                continue 
            
            # 웅덩이일 경우, 0으로 만들어줌
            if [i, j] in puddles:    
                dp[i][j] = 0
            # 현재 칸까지 올 수 있는 경우의 수를 구하기 위해 (현재 칸 = 왼쪽 칸 + 위쪽 칸)
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]