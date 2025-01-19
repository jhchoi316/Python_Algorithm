import sys
read = sys.stdin.readline

K, N = map(int, read().strip().split())
LANs = [int(read().strip()) for _ in range(K)]

start, end = 1, max(LANs)

while start <= end:
    mid = (start+end) // 2
    
    tmp = 0
    for i in LANs:
        tmp += i//mid
    
    if tmp >= N:
        start = mid +1
    else:
        end = mid - 1

print(end)