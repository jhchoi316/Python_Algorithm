import sys

n = int(sys.stdin.readline())
numList = []

for i in range(n):
    k = int(sys.stdin.readline())
    
    if k != 0:
        numList.append(k)
    else:
        numList.pop()
        
print(sum(numList))