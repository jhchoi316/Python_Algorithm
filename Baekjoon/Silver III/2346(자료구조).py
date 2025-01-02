import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
queue = deque(enumerate(map(int, read().strip().split())))
ans = []

while queue:
    idx, flag = queue.popleft()
    ans.append(idx + 1)

    if flag > 0:
        queue.rotate(-(flag - 1))
    elif flag < 0:
        queue.rotate(-flag)

print(' '.join(map(str, ans)))