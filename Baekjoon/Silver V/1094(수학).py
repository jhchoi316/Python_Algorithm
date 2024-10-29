x = int(input())

sticks = [64]

count = 1

while sum(sticks) != x:
    sticks.sort()
    
    tmp = sticks.pop(0)
    tmp //= 2
    
    sticks.append(tmp)
    
    if sum(sticks) < x:
        sticks.append(tmp)

print(len(sticks))