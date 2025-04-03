import sys
read = sys.stdin.readline

N = int(read())
switch = [0]
INPUT = list(map(int, read().split()))
switch.extend(INPUT)
M = int(read())

def toggle(index):
    if switch[index] == 1:
        switch[index] = 0
    else:
        switch[index] = 1

def check(i, j):
    if switch[i] == switch[j]:
        return True
    else:
        return False

for i in range(M):
    sex, num = map(int, read().split())

    # 남학생 -> 자기 번호의 배수면 스위치 toggle
    if sex == 1:
        for i in range(1, (N//num)+1):
            index = i * num
            toggle(index)
    
    # 여학생 -> 자기 번호 기준으로 좌우 대칭 + 가장 많은 구간 toggle
    else:
        toggle(num)
        for i in range(1, N):
            if num - i < 1 or num + i > N:
                break
            if check(num-i, num+i):
                toggle(num-i)
                toggle(num+i)
            else:
                break
            
for i in range(1, N+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()