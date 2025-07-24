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
        # 종료 조건(불가능), 시작이 아니거나 사이클이 있거나
        if a not in graph or a in visited:
            print("F")
            break
        # 종료 조건(가능)
        if graph[a] == b:
            print("T")
            break
        # 이행적 관계
        visited.add(a)
        a = graph[a]