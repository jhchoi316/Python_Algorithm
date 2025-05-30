import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
tree = list(map(int, read().split()))
idx = int(read())

def remove(x, tree):
    tree[x] = -100
    for i in range(len(tree)):
        if tree[i] == x:
            remove(i, tree)

remove(idx, tree)
answer = 0

for i in range(len(tree)):
    if tree[i] != -100 and i not in tree:
        answer += 1
print(answer)