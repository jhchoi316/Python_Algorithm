import sys
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().strip().split()))

for i in range(N-1, 0, -1):
    if INPUT[i] < INPUT[i-1]:
        for j in range(N-1, 0, -1):
            if INPUT[i] < INPUT[i-1]:
                INPUT[j], INPUT[i-1] = INPUT[i-1], INPUT[j]
                INPUT = INPUT[:i]+sorted(INPUT[i:], reverse=True)

                print(*INPUT)
                exit()
print(-1)