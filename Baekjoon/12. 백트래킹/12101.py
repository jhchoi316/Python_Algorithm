def recursion(x):
    global count, flag
    
    if flag:
        return
    # 합이 n을 넘어갔을 때
    if len(result) > n:
        return
    
    if x > 0:
        # 합이 n이 됐을 때
        if sum(result) == n:
            # 사전 순으로 몇 번쨰 인지 count
            count += 1
            
            # 정답을 찾았을 때
            if count == k:
                print('+'.join(map(str, result)))
                flag = True
                return
    
    # 합은 계속 증가시켜주면서, 정답 출력용 result에 계속 숫자 쌓아주기
    for i in (1, 2, 3):
        result.append(i)
        recursion(x+i)
        result.pop()


n, k = map(int, input().split())
count = 0
result = []
flag = False

recursion(0)

if not flag:
    print(-1)