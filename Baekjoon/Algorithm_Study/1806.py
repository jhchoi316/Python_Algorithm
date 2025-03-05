import sys
read = sys.stdin.readline

N, S = map(int, read().split())
INPUT = list(map(int, read().split()))

# 합 저장
partial_sum = 0
left, right = 0, 0
result = sys.maxsize

while True:
    # 부분합이 S보다 크거나 같으면
    if partial_sum >= S:
        result = min(result, right-left)
        partial_sum -= INPUT[left]
        left += 1

    elif right == N:
        break
    # 부분합이 S보다 작으면
    else:
        partial_sum += INPUT[right]
        right += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)
