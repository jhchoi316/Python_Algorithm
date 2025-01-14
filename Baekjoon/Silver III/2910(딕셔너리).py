import sys
read = sys.stdin.readline

N, C = map(int, read().strip().split())
message = list(map(int, read().strip().split()))

count = {}
index = 1

for i in message:
    if i in count:
        count[i][0] += 1
    else:
        count[i] = [1, index]
        index += 1

tmp = [[i,j] for i,j in count.items()]
tmp.sort(key = lambda x: (-x[1][0], x[1][1]))

result = []
for i, j in tmp:
    result += [i]*j[0]

print(*result)