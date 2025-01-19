import sys
read = sys.stdin.readline

N, M = map(int, read().strip().split())
trees = list(map(int, read().strip().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start+end)//2
    tmp = 0
    
    for i in trees:
        if i >= mid:
            tmp += i - mid

    if tmp >= M:
        start = mid + 1
    else:
        end = mid -1

print(end)