T = int(input())

for t in range(1, T+1):
    M = int(input())
    line = list(map(int, input().split()))
    answer = 0
    max_num = 0
    line = reversed(line)
    
    for i in line:
        if i >= max_num:
            max_num = i
        else:
            answer += max_num - i
            
    print(f"#{t} {answer}")