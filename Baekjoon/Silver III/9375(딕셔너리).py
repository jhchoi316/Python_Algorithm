import sys
read = sys.stdin.readline

T = int(read().rstrip())

for i in range(T):
    N = int(read().rstrip())
    clothes = {}
    
    for j in range(N):
        name, type = read().strip().split()
        
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]
        
    count = 1
    
    for x in clothes:
        count *= (len(clothes[x]) + 1)
        
    print(count-1)