from collections import deque

n, k = map(int, input().split())

durability = deque(map(int, input().split()))
isRobot = deque([False]*n)
step = 0

while True:
    step += 1
    
    # 벨트 회전 
    durability.rotate(1)
    isRobot[-1] = False
    isRobot.rotate(1)
    isRobot[-1] = False

    # 로봇 이동 (n-1 ~ 0)
    for i in range(n-1, 0, -1):
        # 전칸에 로봇이 있고, 현재칸의 내구도가 0이 아니고, 로봇이 없으면 -> 현재칸 내구도 감소, 로봇 이동
        if isRobot[i-1] and durability[i] > 0 and not isRobot[i]:
            durability[i] -= 1
            isRobot[i-1] = False
            isRobot[i] = True

    # 내리는 위치에 로봇이 있다면 내리기
    isRobot[-1] = False
        
    # 올리는 위치에 내구도 0이 아니면, 로봇 올리기
    if durability[0] > 0:
        durability[0] -= 1
        isRobot[0] = True

        
    if durability.count(0) >= k:
        break

print(step)

