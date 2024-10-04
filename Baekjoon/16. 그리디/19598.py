import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().rstrip().split())))

meetings.sort(key = lambda x: x[0])
cnt = 1

b = [0]

for start ,end in a:
    if start >= b[0]:
        heapq.heappop(b)
    else:
        cnt+=1
    heapq.heappush(b, end)

print(cnt)