import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

ans = [0,0]
for i in range(n):
    r_count,c_count = 0,0
    
    for j in range(n):
        if board[i][j] == '.':
            r_count+=1
        else:
            r_count=0
            
        if r_count==2:
            ans[0] += 1
        
        if board[j][i] == '.':
            c_count+=1
        else:
            c_count=0
    
        if c_count==2:
            ans[1] += 1
            
print(*ans)