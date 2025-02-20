import sys
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().split()))
INPUT.sort()

result = 0

for i in range(N):
    target = INPUT[i]
    
    start = 0
    end = N-1
    
    while start < end:
        # 찾았을 떄,
        if INPUT[start]+ INPUT[end] == target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                result += 1
                break
        # 합이 클 때
        elif INPUT[start] + INPUT[end] > target:
            end -= 1
        # 합이 작을 때
        elif INPUT[start] + INPUT[end] < target:
            start += 1

print(result)