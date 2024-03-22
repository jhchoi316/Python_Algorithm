mulNum = 1

for i in range(3):
    mulNum *= (int(input()))
    
numList = list(map(int,str(mulNum)))

print(numList)
for i in range(10):
    print(numList.count(i))