N = int(input())
ropes = []

for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)

res = []
for i in range(N):
    res.append(ropes[i]*(i+1))

print(max(res))