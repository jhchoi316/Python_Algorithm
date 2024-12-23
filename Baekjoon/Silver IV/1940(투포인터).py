import sys
read = sys.stdin.readline

n = int(read())
m = int(read())

materials = list(map(int, read().split()))
materials.sort()

start, end = 0, n-1
result = 0

while start < end:
    tmp = materials[start] + materials[end]

    if tmp > m:
        end -= 1
    elif tmp == m:
        result += 1
        start += 1
    else:
        start += 1
        
print(result)
