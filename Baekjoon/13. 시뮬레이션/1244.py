def toggle(index):
    if switches[index] == 1:
        switches[index] = 0
    else:
        switches[index] = 1
    
n = int(input())
switches = [0]
switches.extend((map(int, input().split())))

s = int(input())
students = [list(map(int, input().split())) for _ in range(s)]

for sex, switch in students:
    # 남자면
    if sex == 1:
        # 전체 스위치 개수 n의 반만 해봐도 전체 경우의 수임
        for i in range(1, n//switch+1):
            # 1->0, 0->1로 바꿈
            toggle(switch*i)
    # 여자면
    if sex == 2:        
        # 자기 자신은 무조건 토글
        toggle(switch)
        
        start, end = switch-1, switch+1
        # 범위 안이고, 대칭일 경우
        while 0 < start and end < n+1 and switches[start] == switches[end]:
            toggle(start)
            toggle(end)
            start -= 1
            end += 1
            
# 출력 조건에 맞춰주자 	
for k in range(1,n+1):
    print(switches[k], end=" ")
    if k % 20 == 0:
        print()