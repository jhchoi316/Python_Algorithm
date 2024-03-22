import sys

n = int(input())
numList = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

result = 0
left = 0
right = n - 1

while left < right:
    tmp = numList[left] + numList[right]

    if tmp == x:
        result += 1
        left += 1
        
    elif tmp > x:
        right -= 1

    else:
        left += 1

print(result)
