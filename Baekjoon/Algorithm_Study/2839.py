import sys
read = sys.stdin.readline

N = int(read())
result = 0

while True:
    if N >= 0:
        if N % 5 == 0:
            result += N//5
            print(result)
            break
        N -= 3
        result += 1
    else:
        print(-1)
        break