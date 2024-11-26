n, kim, lim = map(int, input().split())
count = 0

while True:
    count += 1
    
    if n%2==0:
        n = n//2
    else:
        n = n//2+1

    kim = kim//2 + kim%2
    lim = lim//2 + lim%2
    
    if kim == lim:
        print(count)
        break
    