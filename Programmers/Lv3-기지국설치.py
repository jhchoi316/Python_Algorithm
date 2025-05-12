def solution(N, stations, W):
    answer = 0
    apt = []
    
    # 기지국 사이에 전파가 안오는 아파트 길이 추가
    for i in range(1, len(stations)):
        apt.append((stations[i]-W-1)-(stations[i-1]+W))
    
    # 첫번째 기지국까지
    apt.append(stations[0]-W-1) 
    # 마지막 기지국까지
    apt.append(N-(stations[-1]+W))  
    stations_range = (2*W)+1
    
    for i in apt:
        if i <= 0:
            continue
        else:
            if (i%stations_range) != 0:
                answer += (i//stations_range) + 1
            else:
                answer += (i//stations_range)

    return answer