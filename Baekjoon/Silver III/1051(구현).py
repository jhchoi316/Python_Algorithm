import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, read().rstrip())) for _ in range(n)]

def find_square(x, y):
    if x > y:
        side = y
    else:
        side = x
    return side

side = find_square(n, m)

if side == 1:
    print(1)
    exit()
else:
    result = 1  

    for i in range(2,side+1):
        tmp = 0
        for j in range(0, n-i+1):
            for k in range(0, m-i+1):
                x, y, z, k = graph[j][k], graph[j][k+i-1], graph[j+i-1][k], graph[j+i-1][k+i-1]
                if x == y == z == k:
                    result = i*i
                    continue

    print(result)