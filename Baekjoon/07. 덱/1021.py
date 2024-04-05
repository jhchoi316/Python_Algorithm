import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))

queue = deque(range(1,int(n)+1))

count = 0

for i in input:
    
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    count+=1
            else: 
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    count+=1

print(count)
    
    
    
    # while len(input) != 0:
    #     # 1
    #     move = queue.popleft()
        
    #     if move != input[i]:
    #         # 2
    #         queue.append(move)
    #         # print(queue)
    #         # 3
    #         queue.appendleft(queue.pop())
    #         count += 2
    #         # print(queue, count)
    #     elif move == input[i]:
    #         input.popleft()
    #         i += 1
    #         # print(input, i)

print(count)

