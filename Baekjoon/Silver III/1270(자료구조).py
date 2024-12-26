import sys
from collections import deque
read = sys.stdin.readline

T = int(read())
result = []

for t in range(T):
    N, M = map(int, read().split())
    queue = deque([])
    arr = list(map(int, read().split()))
    count = 0
    
    for i in range(N):
        queue.append([arr[i],i])
        
    if len(queue) == 1:
        print(1)
    else:
        while True:
            max_num = max(queue)
            x = queue.popleft()
            if x[0] != max_num[0]:
                queue.append(x)
            else:
                count += 1
                if x[1] == M:
                    print(count)
                    break