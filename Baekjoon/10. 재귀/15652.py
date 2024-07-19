N, M = list(map(int, input().split()))
answer = []

def func(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(start, N+1):
        answer.append(i)
        func(start)
        answer.pop()
        start += 1

func(1)