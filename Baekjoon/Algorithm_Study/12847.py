import sys
read = sys.stdin.readline

N, M = map(int, read().split())
INPUT = list(map(int, read().split()))

result = []
tmp = sum(INPUT[0:M])
result.append(tmp)

for i in range(M, N):
    a = INPUT[i-M]
    b = INPUT[i]
    
    tmp += b - a
    result.append(tmp)
    
print(max(result))