import sys
read = sys.stdin.readline

n = int(input())
result = 0

for i in range(len(str(n))):
    digit = n%10
    n //= 10
    
    if digit > 4:
        result += (digit-1) * (9**i)
    else:
        result += digit * (9**i)

print(result)