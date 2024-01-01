in1 = list(map(int,input()))

num_count = [0]*9
count = 0

for i in in1:
    if i != 6 and i != 9:
        num_count[i] += 1
    else:
        num_count[6] += 1
    
print(num_count)

for i in range(len(num_count)):
    if i != 6 and num_count[i] > count:
            count = num_count[i]
    elif i==6 and num_count[i] > count * 2:
            if num_count[i] % 2 == 0:
               count = int(num_count[i]/2)
            else:
                count = int((num_count[i]/2) + 1)
    
print(count)

