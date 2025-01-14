import sys
read = sys.stdin.readline

N, X = map(int, read().strip().split())
visiter = list(map(int, read().strip().split()))
sum_visiter = [0 for _ in range(N-X+1)]
sum_visiter[0] = sum(visiter[0:X])

index = 1

for i in range(X, N):
    sum_visiter[index] = sum_visiter[index-1] + visiter[i] - visiter[index-1]
    index += 1
    
max_visiter = max(sum_visiter)

if max_visiter:
    print(max_visiter)
    print((sum_visiter.count(max_visiter)))
else:
    print("SAD")