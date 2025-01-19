import sys
read = sys.stdin.readline

N, S = map(int, input().split())
INPUT = list(map(int, input().split()))
count = 0
result = []

def dfs(index):
    global count
    if sum(result) == S and len(result) > 0:
        count += 1

    for i in range(index, N):
        result.append(INPUT[i])
        dfs(i+1)
        result.pop()

dfs(0)
print(count)