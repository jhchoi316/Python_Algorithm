import sys
read = sys.stdin.readline

n = int(read())
tips = [int(read()) for _ in range(n)]
result = 0
tips.sort(reverse=True)

for i in range(n):
    tip = tips[i] - i
    
    if tip > 0:
        result += tip

print(result)