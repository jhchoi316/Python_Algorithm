import sys
read = sys.stdin.readline

N = int(read().strip())
extensions = []

for i in range(N):
    INPUT = list(read().strip().split("."))
    extensions.append(INPUT[1])

extensions.sort()
result = {}

for i in extensions:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for i, j in result.items():
    print(i, j)