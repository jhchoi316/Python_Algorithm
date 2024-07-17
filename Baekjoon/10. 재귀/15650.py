N, M = list(map(int, input().split()))
answer = []

def combination(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(start, N+1):
        if i not in answer:
            answer.append(i)
            combination(i+1)
            answer.pop()

combination(1)