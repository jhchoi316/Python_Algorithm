def solution(arr):
    answer = max(arr)
    
    while True:
        count = 0
        for i in arr:
            if answer % i == 0:
                count += 1
            else:
                break
        
        if count == len(arr):
            break
        answer += 1
    
    return answer
