def solution(answers):
    supo1 = [1,2,3,4,5] * len(answers)
    supo2 = [2,1,2,3,2,4,2,5] * len(answers)
    supo3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    answer = []
    tmp = []
    
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == supo1[i]:
            cnt += 1
    tmp.append(cnt)
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == supo2[i]:
            cnt += 1
    tmp.append(cnt)
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == supo3[i]:
            cnt += 1
    tmp.append(cnt)
    
    for i in range(len(tmp)):
        if max(tmp) == tmp[i]:
            answer.append(i+1)
            
    return answer