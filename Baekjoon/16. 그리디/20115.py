import sys
read = sys.stdin.readline

n = int(read())
drinks = list(map(int, read().split()))

drinks.sort()
answer = drinks[-1] + (sum(drinks[0:-1])/2)
print(answer)
