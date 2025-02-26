import sys
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().split()))
stack = [0]
result = [-1]*N

for i in range(1, N):
    while stack and INPUT[stack[-1]] < INPUT[i]:
        result[stack.pop()] = INPUT[i]
    stack.append(i)

print(*result)