import sys
read = sys.stdin.readline

row, col = map(int, read().rstrip().split())
floor = [list(read().rstrip()) for _ in range(row)]
result = 0

for i in range(row):
    count = 0
    for j in range(col):
        if floor[i][j] == '-':
            count += 1
        else:
            if count != 0:
                result += 1
                count = 0
    if count != 0:
        result += 1

for i in range(col):
    count = 0
    for j in range(row):
        if floor[j][i] == '|':
            count += 1
        else:
            if count != 0:
                result += 1
                count = 0
    if count != 0:
        result += 1
        
print(result)