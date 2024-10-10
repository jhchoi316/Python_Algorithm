colors = (map(int, input().split()))

count = 0
tmp = []

for c in colors:
    q, r = c//3, c%3
    count += q
    if r:
        tmp.append(r)

if len(tmp) == 1:
    count += 1
elif len(tmp) > 1:
    count += max(tmp)

print(count)