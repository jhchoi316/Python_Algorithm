import sys
read = sys.stdin.readline

n = int(read())
arr = [int(read()) for _ in range(n)]
arr_sorted = sorted(arr)
result = 0

if n == 1:
    print(1)
    exit()

for i in range(n):
    for j in range(n):
        if arr[i] == arr_sorted[j]:
            arr_sorted[j] = 10000
            break
    # 죄소일경우
    if j == 0:
        if arr_sorted[j+1] != 10000:
            result += 1
    # 최대일경우
    elif j == n-1:
        if arr_sorted[j-1] != 10000:
            result += 1
    # 앞뒤가 정렬이 되어있을 경우
    elif arr_sorted[j-1] == 10000 or arr_sorted[j+1] == 10000:
        continue
    else:
        result += 1

print(result)