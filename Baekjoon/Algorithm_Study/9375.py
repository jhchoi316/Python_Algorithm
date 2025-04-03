import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N = int(read())
    fashion = {}
    
    for i in range(N):
        INPUT = list(read().strip().split())
        
        if INPUT[1] in fashion:
            fashion[INPUT[1]].append(INPUT[0])
        
        else:
            fashion[INPUT[1]] = [INPUT[0]]
    
    count = 1
    for j in fashion:
        count *= (len(fashion[j])) + 1

    print(count - 1)