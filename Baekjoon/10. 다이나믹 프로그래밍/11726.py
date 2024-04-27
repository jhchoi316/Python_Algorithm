n = int(input())

graph = [0] * 1001

graph[2] = 2 
graph[3] = 3
graph[4] = 5

for i in range(5, 1001):
    graph[i] = graph[i-2] + graph[i-1]

print(int(graph(n) % 10007))