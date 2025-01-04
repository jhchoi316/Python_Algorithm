import sys
read = sys.stdin.readline

N = int(read())

serial = [read().strip() for _ in range(N)]

def sum_num(serial):
    result = 0
    for i in serial:
        if i.isdigit():
            result += int(i)
    return result

serial.sort(key = lambda x: (len(x), sum_num(x), x))

for i in serial:
    print(i)
