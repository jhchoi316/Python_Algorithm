import sys
read = sys.stdin.readline

S = read().strip()
result = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        result.add(S[i:j+1])

print(len(result))