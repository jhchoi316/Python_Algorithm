numbers = []
for i in range(9):
    numbers.append(int(input()))
    
numbers.sort()

sum = sum(numbers)
fake_numbers = []

for i in range(9):
    for j in range(i+1, 9):
        if len(fake_numbers)==2:
            continue
        if sum-numbers[i]-numbers[j] == 100:
            fake_numbers.append(numbers[i])
            fake_numbers.append(numbers[j])

for i in numbers:
    if i in fake_numbers:
        continue
    print(i)