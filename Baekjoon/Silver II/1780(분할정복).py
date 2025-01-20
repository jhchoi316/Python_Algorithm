import sys
read = sys.stdin.readline

N = int(read())
graph = [read().strip().split() for _ in range(N)]
result = {'-1':0, '0':0, '1':0}

def divAndCon(row, col, n):
    curr = graph[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if graph[i][j] != curr:
                next = n //3
                divAndCon(row, col, next)
                divAndCon(row, col+next, next)
                divAndCon(row, col+(next*2), next)
                divAndCon(row+next, col, next)
                divAndCon(row+next, col+next, next)
                divAndCon(row+next, col+(next*2), next)
                divAndCon(row+(next*2), col, next)
                divAndCon(row+(next*2), col+next, next)
                divAndCon(row+(next*2), col+(next*2), next)
                return
    result[str(curr)] += 1
    return

divAndCon(0,0,N)

for i in result.values():
    print(i)