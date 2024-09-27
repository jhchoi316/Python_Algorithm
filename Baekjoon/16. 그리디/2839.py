n = int(input())

count = 0

while True:
    if n == 1 or n == 2 or n == 4:
        print(-1)
        break 
    
    if n % 5 == 0:
        print(count + n//5)
        break 
    
    n -= 3
    count += 1