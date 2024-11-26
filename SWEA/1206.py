
for t in range(1, 11):
    n = int(input())
    apt = list(map(int, input().split()))
    answer = 0
    
    for i in range(2, n-2):
        building = apt[i-2:i+3]
        print(building)
        if max(building) == apt[i]:
            building.sort(reverse=True)
            answer += building[0]-building[1]
            
    print(f"#{t} {answer}")