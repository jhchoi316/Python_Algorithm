N = int(input())

def star(N):
    if N == 1:
        return ['*']
    
    stars = star(N//3)
    
    result = []
    
    for i in stars:
        result.append(i * 3)
    
    for i in stars:
        result.append(i + ' ' * (N//3) + i)
        
    for i in stars:
        result.append(i * 3)
    
    return result

answer = star(N)

for i in answer:
    print(i)