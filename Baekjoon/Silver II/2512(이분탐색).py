import sys
read = sys.stdin.readline

N = int(read())
INPUT = sorted(list(map(int, read().strip().split())))
budget = int(read())

start = 0
end = INPUT[-1]
result = 0

while start <= end:
    mid = (start+end) // 2
    tmp = 0

    for i in INPUT:
        if i > mid:
            tmp += mid
        else:
            tmp += i
    
    if tmp <= budget:
        result = mid
        start = mid + 1
    else:
        end = mid -1
        
print(result)