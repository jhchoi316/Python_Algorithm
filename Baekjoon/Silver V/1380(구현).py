
scenario = 0

while True:
    scenario += 1
    n = int(input())
    
    if n == 0:
        exit()
        
    students = []
    num = [0 for _ in range(n)]
    
    for i in range(n):
        s = input()
        students.append([i, s])
    
    for i in range((2*n-1)):
        x, y = input().split()
        x = int(x)-1
        num[x] += 1
            
    for i in range(n):
        if num[i] == 1:
            print(scenario, students[i][1])