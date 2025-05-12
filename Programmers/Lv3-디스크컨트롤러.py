import heapq

def solution(jobs):
    answer = 0
    # 현재시간
    now = 0 
    # 처리개수
    count = 0   
    # 마지막 완료시간
    start = -1 
    heap = []
    
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            # 요청으로부터 처리시간
            answer += now - current[1] 
            count += 1
        else:
            now += 1
            
    return answer // len(jobs)
