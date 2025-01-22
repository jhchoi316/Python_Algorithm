import sys
read = sys.stdin.readline

N = int(read())
dp = [0]*(N+1)

dp[1] = 1

for i in range(2, N+1):
    sqrt = int(i**0.5)
    print(i, i-sqrt**2)
    if i - sqrt**2 == 0:
        dp[i] = 1
    else:
        dp[i] = dp[sqrt**2] + dp[i-sqrt**2]
    
print(dp)
print(dp[N])