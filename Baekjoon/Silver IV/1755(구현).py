import sys
read = sys.stdin.readline
alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

m, n = map(int, read().split())
result = [[i//10, i%10] for i in range(m, n+1)]

for i in range(len(result)):
    if result[i][0] != 0:
        tmp = alpha[result[i][0]] + alpha[result[i][1]]
        result[i].append(tmp)
    else:
        result[i].append(alpha[result[i][-1]])

result.sort(key= lambda x: x[-1])

answer = []
for i in range(len(result)):
    answer.append(result[i][0]*10+result[i][1])

count = 0
i = 0
while i < len(answer):
    if count == 10:
        print()
        count = 0
    else:
        print(''.join(str(answer[i])), end=" ")
        i += 1
        count += 1
