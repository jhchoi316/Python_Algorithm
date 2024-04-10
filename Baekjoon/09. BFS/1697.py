import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

MAX = 100001
visited = [0] * MAX

def bfs():
    queue = deque()
    # 출발점 queue에 삽입
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        # 찾았을 때 break
        if x == k:
            print(visited[x])
            break
        # 이동할 수 있는 방향에 대해 for문 실행
        for i in (x-1, x+1, 2*x):
            # 주어진 범위 안에 있고, 아직 방문하지 않았다면
            if -1< i < MAX and not visited[i]:
                # 이동한 위치에 현재 이동한 시간 표시
                visited[i] = visited[x] + 1
                queue.append(i)

bfs()