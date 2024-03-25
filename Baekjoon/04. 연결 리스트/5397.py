n = int(input())
result = []

for i in range(n):
    inputStr = list(input())
    stack_l = []
    stack_r = []
    
    if '<' or '>' or '-' in inputStr:
        for i in range(len(inputStr)):
            if inputStr[i] == '<' and stack_l:
                stack_r.append(stack_l.pop())
            elif inputStr[i] == '>' and stack_r:
                stack_l.append(stack_r.pop())
            elif inputStr[i] == '-' and stack_l:
                stack_l.pop()
            elif inputStr[i] != '<' and inputStr[i] != '>' and inputStr[i] != '-':
                stack_l.append(inputStr[i])
            else:
                continue
        result.append(''.join(stack_l + list(reversed(stack_r))))
    else:
        result.append(stack_l)

for i in range(len(result)):
    print(result[i])

        
