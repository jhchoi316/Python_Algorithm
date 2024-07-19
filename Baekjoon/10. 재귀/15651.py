N, M = list(map(int, input().split()))
answer = []

def func():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        answer.append(i)
        func()
        answer.pop()

func()