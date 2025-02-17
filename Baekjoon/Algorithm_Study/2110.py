import sys
read = sys.stdin.readline

N, C = map(int, read().split())
house = []

for i in range(N):
    house.append(int(read()))
house.sort()

result = 0

# 최소 거리
start = 1
# 최대 거리
end = house[-1] - house[0]

while start <= end :
    # 공유기 설치할 수 있는 거리가 mid로 설정
    mid = (start + end) // 2
    # 맨 앞 집부터 시작
    cur_house = house[0]
    # 공유기 개수
    count = 1

    # 거리를 mid로 할 경우
    # 현재 집에서 거리보다 크면 설치 가능
    # 작으면 설치 불가능
    for i in range(1, N):
        print(house[i], cur_house+mid)
        if house[i] >= cur_house + mid:
            # 하나 설치
            count += 1
            # 현재 집에 공유기 설치
            cur_house = house[i]
    
    # 설치한 공유기 개수가 C보다 크면
    # 더 넒게 설치 할 수 있음
    if count >= C:
        start = mid + 1
        result = mid
    # 더 좁게 설치 해야함 
    else:
        end = mid - 1
        
print(result)

