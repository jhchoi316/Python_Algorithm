import sys
read = sys.stdin.readline

n, m = map(int, read().split())
hear = set()
see = set()
result = []

for _ in range(n):
    hear.add(read().rstrip())

for _ in range(m):
    see.add(read().rstrip())

result = sorted(list(hear&see))

print(len(result))
print(result)
for i in result:
    print(i)