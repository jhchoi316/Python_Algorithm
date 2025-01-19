import sys
import heapq
read = sys.stdin.readline

N = int(read().strip())
heap = []

for _ in range(N):
    x = int(read().strip())
    
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)