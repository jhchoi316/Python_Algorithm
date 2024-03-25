N, K = map(int, input().split())
queue = list(range(1, N+1))
index = 0
result = []

for i in range(N):
    index += K-1
    if index >= len(queue):
        index = index%len(queue)
    
    result.append(str(queue.pop(index)))
    
print("<",", ".join(result)[:],">", sep='')