import sys
read = sys.stdin.readline

N = int(read().strip())
INPUT = list(map(int, read().strip().split()))

for i in range(N-1, 0, -1):
    if INPUT[i-1] < INPUT[i]:
        for j in range(N-1, 0, -1):
            if INPUT[i-1] < INPUT[j]:
                INPUT[i-1], INPUT[j] = INPUT[j], INPUT[i-1]
                INPUT = INPUT[:i] + sorted(INPUT[i:])
                
                print(*INPUT)
                exit()
print(-1)