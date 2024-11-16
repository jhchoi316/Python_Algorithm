T = int(input())

for test_case in range(1, T + 1):
    line = list(map(int, input().split()))
    answer = 0
    for i in line:
        if i%2 == 1:
            answer += i
    print(f"#{test_case} {answer}")
