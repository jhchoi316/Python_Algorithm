import sys
import heapq
read = sys.stdin.readline

N = int(read())
heap = []

for i in range(N):
    x = int(read())

    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)