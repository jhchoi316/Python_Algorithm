import sys
read = sys.stdin.readline

n = int(read())
cost = []
delivery = []

for i in range(n):
    c, d = map(int, read().split())
    cost.append(c)
    delivery.append(d)

cost_set = sorted(set(cost))

max_num = 0
result = 0

for i in cost:
    money = 0
    for j in range(n):
        if i <= cost[j] and i > delivery[j]:
            money += i - delivery[j]
    
    if max_num < money:
        max_num = money
        result = i

print(result)