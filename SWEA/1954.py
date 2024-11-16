T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for t in range(1, T+1):
    n = int(input())
    snail = [[0]*(n) for _ in range(n)]
    i = 0
    j = 0
    direction = 0
    
    for k in range(1, n*n+1):
        snail[i][j] = k
        i += dx[direction]
        j  += dy[direction]
        
        if i < 0 or j < 0 or i >= n or j >= n or snail[i][j]!= 0:
            i -= dx[direction]
            j -= dy[direction]
            direction = (direction+1) % 4
            i += dx[direction]
            j  += dy[direction]
    
    print(f"#{t}")
    for i in snail:
        print(*i)