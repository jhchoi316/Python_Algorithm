N = int(input())
dp = [0] * 100001

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
            
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
            
res = [N]
now = N
tmp = dp[N]-1

for i in range(N,0,-1):
    print(now, tmp, dp[i])
    if dp[i] == tmp and (i+1 == now or i*2==now or i*3==now):
        now = i
        res.append(i)
        tmp -= 1
        

print(dp[N])
print(*res)