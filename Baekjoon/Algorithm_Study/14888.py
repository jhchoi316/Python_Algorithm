import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))
op = list(map(int, read().split()))

max_answer = -1e9
min_answer = 1e9

def backtracking(depth, tmp, plus, minus, multiply, division):
    global max_answer, min_answer
    
    # 종료 조건
    if depth == len(arr):
        max_answer = max(tmp, max_answer)
        min_answer = min(tmp, min_answer)
        return

    if plus:
        backtracking(depth+1, tmp + arr[depth], plus-1, minus, multiply, division)
    if minus:
        backtracking(depth+1, tmp-arr[depth], plus, minus-1, multiply, division)
    if multiply:

        backtracking(depth+1, tmp*arr[depth], plus, minus, multiply-1, division)
    if division:
        backtracking(depth+1, int(tmp/arr[depth]), plus, minus, multiply, division-1)

backtracking(1, arr[0], op[0], op[1], op[2], op[3])

print(max_answer)
print(min_answer)