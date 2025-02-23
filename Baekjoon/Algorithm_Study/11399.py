import sys
read = sys.stdin.readline

N = int(read())
time = sorted(list(map(int, read().split())))

result = 0

for i in range(len(time)):
    for j in range(i+1):
        result += time[j]

print(result)