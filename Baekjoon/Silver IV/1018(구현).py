n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
count = []

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        
        for k in range(i, i+8):
            for z in range(j, j+8):
                if (k+z)%2==0:
                    if board[k][z]!='W':
                        white+=1
                    else:
                        black+=1
                else:
                    if board[k][z]!='W':
                        black+=1
                    else:
                        white+=1
                
        count.append(white)
        count.append(black)

print(count)
print(min(count))