import sys
read = sys.stdin.readline

T = int(read())

for i in range(T):
    N, M = map(int, read().split())
    A = sorted(list(map(int, read().split())))
    B = sorted(list(map(int, read().split())))

    result = 0
    
    for a in A:
        start, end = 0, len(B)-1
        tmp = -1
        
        while start <= end:
            mid = (start + end) // 2
            if B[mid] < a:
                tmp = mid
                start = mid + 1
                
            else:
                end = mid - 1
        result += tmp + 1
    
    print(result)