n, m = map(int, input().split())
books = list(map(int, input().split()))
count = 0
tmp = m

if n > 0:
    for i in range(n):
        if tmp - books[i] >= 0:
            tmp -= books[i]
        else:
            count += 1
            tmp = m
            tmp -= books[i]
            
    print(count+1)
else:
    print('0')
