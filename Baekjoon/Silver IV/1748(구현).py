import sys
read = sys.stdin.readline

n = int(read())
length = len(str(n))
result = 0
tmp = 0

while True:
    tmp = n - (10**(length-1)) + 1
    result += tmp * length
    n -= tmp
    length -= 1
    
    if length == 0:
        print(result)
        break


# n = 120 
# tmp = (120-100+1) = 21
# n = 21*3 = 63
# n = 120-21 = 99

# n = 99
# tmp = (99-10+1) = 90
# n = 90*2 = 180
# n = 99-90 = 9

