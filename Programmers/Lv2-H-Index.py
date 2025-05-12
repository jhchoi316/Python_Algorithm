def solution(citations):
    sort_list = sorted(citations, reverse = True)
    
    for i in range(len(sort_list)):
        if sort_list[i] < i+1:
            return i

    return len(citations)