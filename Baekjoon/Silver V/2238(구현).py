u, n = map(int, input().split())
humans = [[] for _ in range(10001)]
costs = [0 for _ in range(10001)]
max_cost = 10001

for _ in range(n):
    name, cost = input().split()
    cost = int(cost)
    humans[cost].append(name)
    costs[cost] += 1

for i in range(10001):
    if costs[i] != 0:
        max_cost = min(costs[i], max_cost)

for i in range(10001):
    if max_cost == costs[i]:
        print(humans[i][0],i)
        break