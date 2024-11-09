x = list(map(int, input()))
tmp = 0
count = 0

while True:
    if len(x) == 1:
        if x[0] == 3 or x[0] == 6 or x[0] == 9:
            print(count)
            print("YES")
        else:
            print(count)
            print("NO")
        break
    
    else:
        for i in x:
            tmp += i
        x = list(map(int, str(tmp)))
        tmp = 0
        count += 1