import sys
from itertools import combinations
read = sys.stdin.readline

n = int(read())
candy = []
result = []
tmp = 0

for _ in range(n):
    candy.append(int(read().rstrip()))

for i, j in enumerate(candy):
    if i%2 ==0:
        tmp += j
    else:
        tmp -= j
result.append(tmp//2)

for i in range(n-1):
    result.append(candy[i]-result[i])

for i in result:
    print(i)