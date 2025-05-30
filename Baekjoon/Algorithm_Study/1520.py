import sys
from collections import deque
sys.setrecursionlimit(10**9)
read = sys.stdin.readline

M, N = map(int, read().split())
graph = [list(map(int, read().strip().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

def is_range(x, y, now):
    return 0 <= x < M and 0 <= y < N and graph[x][y] < now

def solution(x, y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_range(nx, ny, graph[x][y]):
                dp[x][y] += solution(nx, ny)
    
    return dp[x][y]

print(solution(0, 0))