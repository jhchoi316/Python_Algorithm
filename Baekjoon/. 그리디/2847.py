N = int(input())

levels = [int(input()) for _ in range(N)]

res = 0
maxNum = levels[-1]

for i in range(len(levels)-2, -1, -1):
    if levels[i] > maxNum:
        res += levels[i] - maxNum + 1
        maxNum -= 1
    elif levels[i] == maxNum:
        res += 1
        maxNum-=1
    elif levels[i] < maxNum:
        maxNum = levels[i]

print(res)