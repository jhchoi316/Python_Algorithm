N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

def quadTree(x, y, N):
    check = graph[x][y]
    
    # 정해진 구간이 모두 같은 숫자인 경우
    for i in range(x, x+N):
        for j in range(y, y+N):
            if graph[i][j] != check:
                check = -1
                break
    
    # 정해진 구간이 모두 같은 숫자가 아닐 경우
    if check == -1:
        print("(", end='')
        N = N//2
        quadTree(x, y, N) # 왼쪽 위
        quadTree(x, y+N, N) # 오른쪽 위
        quadTree(x+N, y, N) # 왼쪽 아래
        quadTree(x+N, y+N, N) # 오른쪽 아래
        print(")", end='')
        
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

quadTree(0, 0, N)