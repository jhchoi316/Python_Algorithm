import sys
read = sys.stdin.readline

n = int(read())
arr = [int(read()) for _ in range(n)]
arr.sort()
result = []

for i in range(n):
    count = 0
    for j in range(arr[i], arr[i]+5):
        if j not in arr:
            count += 1
    result.append(count)
    
print(min(result))