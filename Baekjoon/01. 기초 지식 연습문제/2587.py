numberList = []

for i in range(5):
    numberList.append(int(input()))

numberList.sort()

print(int(sum(numberList)/len(numberList)))
print(numberList[int(len(numberList)/2)])