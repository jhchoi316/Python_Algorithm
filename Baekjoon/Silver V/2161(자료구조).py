from collections import deque

n = int(input())
result = []

queue = deque(i for i in range(1,n+1))

while len(queue) != 1:
    result.append(queue.popleft())
    queue.append(queue.popleft())

result.append(queue.pop())
print(' '.join(map(str,result)))