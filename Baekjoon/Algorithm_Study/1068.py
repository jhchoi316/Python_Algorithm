import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
tree = list(map(int, read().split()))
graph = [[] for _ in range(N)]

for i in range(len(tree)):
    if tree[i] == -1:
        graph[i].append(tree[i])
    else:
        graph[i].append(tree[i])
        

def remove(x, next):
    if next == -1:
        return
    graph.remove(graph[x])
    for i in range(len(graph)):
        if graph[i] == x:
            next = graph[i]
            graph.remove(graph[i])
            remove(next)

remove(int(read()), -2)
print(graph)