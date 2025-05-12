from collections import deque

def solution(board):
    def bfs(start):
        # 상,우,하,좌 순서
        direction = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]} 
        visited = [[987654321] * len(board) for _ in range(len(board))]
        visited[0][0] = 0

        queue = deque([start]) # x, y, 비용, 방향
        while queue:
            x, y, cost, d = queue.popleft()
            
            for i in range(4): # 상,우,하,좌 순서
                nx = x + direction[i][0]
                ny = y + direction[i][1]

                # board 안에 있고, 벽이 아닌지 확인
                if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                    
                    # 같은방향-직진
                    if i == d : 
                        ncost = cost + 100
                    # 다른 방향-꺽기
                    else : 
                        ncost =  cost + 600
                    
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        queue.append([nx, ny, ncost, i])
                        
        return visited[-1][-1]
    
    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])