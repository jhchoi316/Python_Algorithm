import sys
read = sys.stdin.readline
sys.setrecursionlimit(100001)

row, col = map(int, read().split())
graph = [[0]*row for _ in range(col)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cur_x, cur_y = 0, 0
num = 1
index = 0

while True:
    if num == row*col:
        print(cur_y, cur_x)
        break
    
    graph[cur_x][cur_y] = 1
    now_x, now_y = cur_x + dx[index], cur_y + dy[index]
    
    if 0<=now_x<col and 0<=now_y<row and graph[now_x][now_y] == 0:
        cur_x, cur_y = now_x, now_y
        num += 1
    else:
        index = (index+1)%4