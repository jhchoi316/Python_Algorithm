import sys
read = sys.stdin.readline

N, K = map(int, read().split())

temperature = list(map(int, read().split()))
sum_temp = sum(temperature[:K])
result = sum_temp

for i in range(N-K):
    sum_temp += temperature[i+K] - temperature[i]
    
    if result < sum_temp:
        result = sum_temp

print(result)
