import sys
read = sys.stdin.readline

S = read().strip()
stack = []
result = ""
flag = False

for i in S:
    if i == '<':
        flag = True
        for _ in range(len(stack)):
            result += stack.pop()

    stack.append(i)
    
    if i == '>':
        flag = False
        for _ in range(len(stack)):
            result += stack.pop(0)
    
    if i == ' ' and flag == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            result += stack.pop()
        result += ' '

if stack:
    for _ in range(len(stack)):
        result += stack.pop()

print(result)