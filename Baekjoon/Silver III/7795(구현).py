import sys
read = sys.stdin.readline

T = int(read())

for t in range(T):
    N, M = map(int, read().strip().split())
    A = sorted(list((map(int, read().strip().split()))))
    B = sorted(list((map(int, read().strip().split()))))
    
    start = 0
    count = 0
        
    for j in range(N):
        
        while True:
            if start==M or A[j]<=B[start]:
                count+=start
                break
            else:   
                start+=1
                
    print(count)