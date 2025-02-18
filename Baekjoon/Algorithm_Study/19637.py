import sys
read = sys.stdin.readline

N, M = map(int, read().split())
titles = [read().split() for _ in range(N)]
titles.sort(key=lambda x : int(x[1]))

characters = [int(read()) for _ in range(M)]

for char in characters:
    start, end = 0, len(titles)
    result = 0
    
    while start <= end:
        mid = (start+end) // 2
        
        if int(titles[mid][1]) >= char:
            result = mid
            end = mid - 1
        else:
            start = mid +1
            
    print(titles[result][0])

