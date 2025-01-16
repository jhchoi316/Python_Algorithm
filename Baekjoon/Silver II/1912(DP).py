import sys
read = sys.stdin.readline

N = int(read().strip())
INPUT = list(map(int, read().strip().split()))

for i in range(1, N):
    INPUT[i] = max(INPUT[i], INPUT[i-1]+INPUT[i])

print(max(INPUT))