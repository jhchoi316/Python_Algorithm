import sys
read = sys.stdin.readline

n, k = map(int, read().split())
w_v = [[0,0]]
bags = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    w_v.append(list(map(int, read().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = w_v[i][0]
        value = w_v[i][1]
        
        if j < weight:
            bags[i][j] = bags[i-1][j]
        else:
            bags[i][j] = max(value + bags[i-1][j-weight], bags[i-1][j])


print(bags[n][k])

