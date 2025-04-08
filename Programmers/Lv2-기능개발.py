def count_days(p, s):
    
    quotient = (100-p)//s
    remain = (100-p)%s
    
    if remain == 0:
        return quotient
    else:
        return quotient + 1

def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        days.append(count_days(progresses[i], speeds[i]))
    
    current = days[0]
    count = 1
    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1
    answer.append(count)
    
    return answer