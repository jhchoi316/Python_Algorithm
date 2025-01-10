import sys
read = sys.stdin.readline

N = int(read())
INPUT = int(read())
graph = [[0]*N for _ in range(N)]

x = (N-1)//2
y = (N-1)//2
graph[x][y] = 1

# 상, 우, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

i = 2
start = 3

while x != 0 or y != 0:
    while i <= start * start:
        if x == y == (N-1)//2:
            count_up, count_down, count_left, count_right = start, start-1, start-1, start-2
            x += dx[0]
            y += dy[0]
            count_up -= 1
        elif count_right > 0:
            x += dx[3]
            y += dy[3]
            count_right -=1
        elif count_down > 0:
            x += dx[1]
            y += dy[1]
            count_down -= 1
        elif count_left > 0:
            x += dx[2]
            y += dy[2]
            count_left -= 1
        elif count_up > 0:
            x += dx[0]
            y += dy[0]
            count_up -= 1
        graph[x][y] = i
        i += 1
    N -= 2
    start += 2

mx = 0
my = 0

for j in range(len(graph)):
    print(*graph[j])
    if INPUT in graph[j]:
        mx = j + 1
        my = graph[j].index(INPUT) + 1

print(mx, my)

