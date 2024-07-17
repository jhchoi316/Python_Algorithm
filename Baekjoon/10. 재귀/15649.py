N, M = map(int, input().split())
answer = []

def permutation():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        answer.append(i)
        permutation()
        answer.pop()
        

permutation()