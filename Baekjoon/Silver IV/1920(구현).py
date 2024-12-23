import sys
read = sys.stdin.readline

n = int(read())
a = set(map(int, read().rstrip().split()))
m = int(read())
check = list(map(int, read().rstrip().split()))
a.sort()

for i in check:
    if i in a:
        print(1) 
    else:   
        print(0)