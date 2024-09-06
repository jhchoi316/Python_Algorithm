import sys

read = sys.stdin.readline
r, c, t = map(int, read().split())
map = [list(map(int, read().split())) for _ in range(r)]

up = -1
down = -1

# 공기 청정기 위치 찾기
for i in range(r):
    if map[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_map = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if map[i][j] != 0 and map[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and map[nx][ny] != -1:
                        tmp_map[nx][ny] += map[i][j] // 5
                        tmp += map[i][j] // 5
                map[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            map[i][j] += tmp_map[i][j]

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        map[x][y], before = before, map[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        map[x][y], before = before, map[x][y]
        x = nx
        y = ny

for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if map[i][j] > 0:
            answer += map[i][j]

print(answer)