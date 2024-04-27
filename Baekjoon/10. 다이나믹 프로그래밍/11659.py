import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = [0]
tmp = 0

for i in arr:
    tmp += i
    res.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    
    print(res[j]-res[i-1])