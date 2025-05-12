def solution(k, tangerine):
    answer = 0
    dict = {}
    for i in range(len(tangerine)):
        if tangerine[i] in dict:
            dict[tangerine[i]] += 1
        else:
            dict[tangerine[i]] = 1
    
    list_dict = [[i,j] for i,j in dict.items()]
    sort_dict = sorted(list_dict, key = lambda x: x[1], reverse=True)

    idx = 0
    
    while k > 0:
        k -= sort_dict[idx][1]
        answer += 1
        idx += 1

    return answer