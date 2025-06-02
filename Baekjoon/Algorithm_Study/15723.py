import sys
read = sys.stdin.readline

N = int(input())
graph = dict()

for i in range(N):
    a, b = list(input().split(" is "))
    graph[a] = b

M = int(input())
for i in range(M):
    a, b = list(input().split(" is "))

    visited = set()
    
    while True:
        if a not in graph or a in visited:
            print("F")
            break
        if graph[a] == b:
            print("T")
            break
        visited.add(a)
        a = graph[a]