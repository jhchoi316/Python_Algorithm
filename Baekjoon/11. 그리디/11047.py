import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
res = 0

for i in range(N):
    x = int(input())
    
    if x <= K:
        coins.append(x)

coins.reverse()

for i in range(len(coins)):
    if coins[i] <= K and K//coins[i] > 0:
        res += K//coins[i]
        K = K - (K//coins[i])*coins[i]

print(res)