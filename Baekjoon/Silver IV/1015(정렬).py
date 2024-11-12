n = int(input())
a = list(map(int, input().split()))

sort_a = sorted(a)

answer = []

for i in range(n):
    answer.append(sort_a.index(a[i]))
    sort_a[sort_a.index(a[i])] = -1

for i in range(n):
    print(str(answer[i]), end = ' ')

