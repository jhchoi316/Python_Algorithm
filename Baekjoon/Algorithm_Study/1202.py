import sys
import heapq
read = sys.stdin.readline

N, K = map(int, read().split())
jewels = []
bags = []

for i in range(N):
    jewels.append(list(map(int, read().split())))

for i in range(K):
    bags.append(int(read()))

jewels.sort()
bags.sort()
tmp = []
result = 0

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(tmp, -jewels[0][1])
        heapq.heappop(jewels)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)