def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n-1))

factorial_list = [factorial(i) for i in range(21)]

n = int(input())

if n == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if n >= factorial_list[i]:
            n -= factorial_list[i]
    
    print("YES") if n == 0 else print("NO")