n = int(input())
count = 0
    
for i in range(n):
    stack = []
    inputStr = list(input())
    for j in range(len(inputStr)):
        if len(stack)==0:
            stack.append(inputStr[j])
        else:
            if inputStr[j]=='A' and stack[-1]=='A':
                stack.pop()
            elif inputStr[j]=='A' and stack[-1]=='B':
                stack.append(inputStr[j])
            elif inputStr[j]=='B' and stack[-1]=='A':
                stack.append(inputStr[j])
            elif inputStr[j]=='B' and stack[-1]=='B':
                stack.pop()
    if len(stack)==0:
        count += 1

print(count)
