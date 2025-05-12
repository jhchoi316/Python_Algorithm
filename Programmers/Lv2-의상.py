
def solution(clothes):
    clothes_dict = {}
    
    for i in clothes:
        if i[1] not in clothes_dict:
            clothes_dict[i[1]] = 1
        else:
            clothes_dict[i[1]] += 1

    answer = 1
    
    for i, j in clothes_dict.items():
        answer *= (j + 1)
        
    return answer - 1
