inputStr = list(input())
stack = []
count = 0

for i in range(len(inputStr)-1):
    # 쇠막대기 시작
    if inputStr[i]=='(' and inputStr[i+1]=='(':
        stack.append(1)
    # 쇠막대기 끝
    elif inputStr[i]==')' and inputStr[i+1]==')':
        stack.pop()
        count += 1
    # 레이저를 의미함
    elif inputStr[i]=='(' and inputStr[i+1]==')':
        count += len(stack)
    else:
        continue
    
print(count)