import sys
read = sys.stdin.readline

n = int(read())

meetings = [list(map(int, read().split())) for _ in range(n)]

meetings.sort(key = lambda x: (x[1], x[0]))

end = meetings[0][1]
count = 1
result = []

for i in range(1, n):
    if meetings[i][0] >= end:
        count += 1
        end = meetings[i][1]

print(count)