import sys
read = sys.stdin.readline

n, m = map(int, read().split())

arr = list(map(int, read().rstrip().split()))
start, end = 0, 1
count = 0

while end<=n and start<=end:
    sum_nums = arr[start:end]
    total = sum(sum_nums)
    
    if total == m:
        count += 1
        end += 1
    elif total < m:
        end += 1
    else:
        start += 1
        
print(count)