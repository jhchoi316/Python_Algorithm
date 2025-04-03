import sys
read = sys.stdin.readline

triangle = list(map(int, read()))


def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0].append(triangle[0][0])
    dp[1].append(dp[0][0]+triangle[1][0])
    dp[1].append(dp[0][0]+triangle[1][1])
    
    for i in range(2, len(triangle)):
        dp[i].append(dp[i-1][0] + triangle[i][0])
        
        for j in range(1, i):
            dp[i].append(triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j]))
                                            
        dp[i].append(dp[i-1][-1] + triangle[i][-1])
    
    return max(dp[-1])