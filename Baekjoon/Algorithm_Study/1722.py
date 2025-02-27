import sys
read = sys.stdin.readline

N = int(read())

possible = [0] * 21
possible[0] = 1
# 각 자리수의 경우의 개수 대입 (N!)
for i in range(1, N+1):
    possible[i] = possible[i-1] * i

used = [False] * 21
result = [0] * 21
INPUT = list(map(int, input().split()))

if INPUT[0] == 1:

    K = INPUT[1]
    for i in range(1, N+1):
        # 자리 수 확인
        count = 1 
        for j in range(1, N+1):
            if used[j]:
                continue
            # 속해 있는 자리수 인지 확인
            if K <= count * possible[N-i]:
                # 남은 경우의 수 대입
                K -= (count-1) * possible[N-i]
                result[i] = j
                used[j] = True
                break
            count += 1

    for i in range(1, N+1):
        print(result[i], end=" ")

else: 

    K = 1
    for i in range(1, N+1):
        count = 0
        # 해당 자리의 수보다 작은 수 중 사용되지 않은 횟수 확인
        for j in range(1, INPUT[i]):
            if not used[j]:
                count += 1

        # 그 회수만큼 이전 가능한 경우의 수를 곱해서 더해줌
        K += count * possible[N-i]
        # 그 자리수 더 이상 사용 불가
        used[INPUT[i]] = True

    print(K)