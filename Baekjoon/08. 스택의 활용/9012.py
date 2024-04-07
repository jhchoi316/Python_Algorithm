T = int(input())

for i in range(T):
    stack = []
    x = list(input())
    
    for j in range(len(x)):
        if len(stack)==0 and x[j]=='(':
            stack.append(x[j])
        elif len(stack)==0 and x[j]==')':
            stack.append(x[j])
            break
        elif x[j]=='(':
                stack.append(x[j])
        elif x[j]==')':
            stack.pop()
            
    if len(stack)==0:
        print('YES')
    else:
        print('NO')