import sys
read = sys.stdin.readline

N = int(read().strip())
rank = sorted([int(read().strip()) for _ in range(N)])

result = 0

for i in range(N):
    result += abs(i+1-rank[i])

print(result)