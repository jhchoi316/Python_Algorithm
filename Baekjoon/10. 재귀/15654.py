N, M = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr.sort()

answer = []

def func():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in arr:
        if i not in answer:
            answer.append(i)
            func()
            answer.pop()

func()
