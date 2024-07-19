N, M = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr.sort()

answer = []

def func(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(start, len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            func(i+1)
            answer.pop()

func(0)