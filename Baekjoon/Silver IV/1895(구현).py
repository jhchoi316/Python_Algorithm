import sys
read = sys.stdin.readline

r, c = map(int, read().rstrip().split())

graph = [list(map(int, read().rstrip().split())) for _ in range(r)]
t = int(read())
j = []

for x in range(r-3+1):
    for y in range(c-3+1):
        median = []
        
        for z in range(x, x+3):
            for u in range(y, y+3): 
                median.append(graph[z][u])
        
        median.sort()
        j.append(median[4])

count = 0 
for k in j:
    if k >= t:
        count += 1

print(count)