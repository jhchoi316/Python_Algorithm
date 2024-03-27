n = int(input())
stack = []

for i in range(n):
    command = list(map(str,input().split()))

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif command[0] == 'top':
        if stack:
            print(int(stack[len(stack)-1]))
        else:
            print('-1')
    
