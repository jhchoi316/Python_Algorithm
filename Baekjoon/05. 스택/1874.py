import sys

n = int(sys.stdin.readline())

count = 1
temp = True
stack = []
result = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    # stack에 들어왔던 가장 높은 수보다 입력값이 크면 입력값까지 push()
    while count <= num:
        stack.append(count)
        result.append('+')
        count+=1
    
    # 스택 가장 위의 값이 현재 입력값이 같으면 pop()
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else: 
    for i in result:
        print(i)