def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))   # 보석 종류 갯수
    left, right = 0, 0 # left는 보석 빼 줄 포인터, right는 보석 더해 줄 포인터
    gem_dict = {gems[0] : 1}
    
    while left < len(gems) and right < len(gems):
        # 딕셔너리에 보석 종류가 다 들어오는 경우
        if len(gem_dict) == size:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]       
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    # count가 0이 되면 key가 없어야하므로 del
                    del gem_dict[gems[left]]    
                left += 1
                
        else:
            right += 1
            
            if right == len(gems):
                break
                
            # 딕셔너리 key에 있으면 count
            if gems[right] in gem_dict: 
                gem_dict[gems[right]] += 1
            
            else:   # 없으면 추가
                gem_dict[gems[right]] = 1
    
    return [answer[0]+1, answer[1]+1]