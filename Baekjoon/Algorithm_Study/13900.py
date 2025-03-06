import sys
read = sys.stdin.readline

N = int(read())
INPUT = list(map(int, read().split()))
result = 0
sum = INPUT.pop()

while INPUT:
    cur_num = INPUT.pop()
    result += sum*cur_num
    sum += cur_num

print(result)
