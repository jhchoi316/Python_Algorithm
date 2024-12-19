import sys
read = sys.stdin.readline

n, m = map(int, read().split())

a = set(map(int, read().rstrip().split()))
b = set(map(int, read().rstrip().split()))

result = list(a-b)

if len(result) == 0:
    print(0)
else:
    print(len(result))
    result.sort()
    for i in result:
        print(i, end=" ")