import sys
read = sys.stdin.readline
n = int(read())

arr = list(map(int, read().split()))
sort_arr = sorted(list(set(arr)))
result = {sort_arr[i] : i for i in range(len(sort_arr))}

for i in arr:
    print(result[i], end=' ')
