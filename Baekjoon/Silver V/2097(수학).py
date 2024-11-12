n = int(input())
result = 0

if n == 0:
    print(0)
elif n == 1:
    print(4)
else:
    i = 0
    while pow(i,2) < n:
        i += 1
    
    if (i-1)*i > n:
        result = (i-2 + i-1) * 2
    else:
        result = (i-1)*4
    
    print(result)
