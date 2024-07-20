N, M = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr.sort()

answer = []

def func():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(len(arr)):
        answer.append(arr[i])
        func()
        answer.pop()
        
func()