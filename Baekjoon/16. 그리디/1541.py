import sys
read = sys.stdin.readline

n = read().rstrip().split("-")
result = 0

for i in range(len(n)):
    tmp = n[i].split("+")
    sum_num = 0
    for j in tmp:
            sum_num += int(j)
    
    
    if i == 0:
        result += sum_num
    else:
        result -= sum_num
    
print(result)