import sys
read = sys.stdin.readline

# 총 대수, 도착 시간
n, t = map(int, read().split())
flag = 0
bus = []
result = []

for _ in range(n):
    s, i, c = map(int, read().split())
    time = [s+(i*j) for j in range(c)]
    
    if time[-1] < t:
        continue
    
    start = 0
    end = c - 1
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        if time[mid] >= t:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    result.append(time[answer] - t)

if result:
    print(min(result))
else:
    print(-1)