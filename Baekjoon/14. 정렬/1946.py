import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    n = int(read())
    arr = [list(map(int, read().split())) for _ in range(n)]
    arr.sort()
    top = 0
    result = 1
    
    for i in range(1, len(arr)):
        if arr[i][1] < arr[top][1]:
            top = i
            result += 1
    
    print(result)