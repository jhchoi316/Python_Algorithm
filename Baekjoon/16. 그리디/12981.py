colors = list(map(int, input().split()))
colors.sort(reverse=True)

min_color = colors.pop()
cnt = min_color
colors = [k-min_color for k in colors]

while sum(colors):
    tmp = colors.pop()
    
    while tmp != 0:
        if tmp > 2:
            cnt += tmp//3
            tmp %= 3
        elif tmp == 2:
            cnt += 1
            tmp %= 2
        elif tmp == 1:
            cnt += 1
            tmp %= 1
            
print(cnt)