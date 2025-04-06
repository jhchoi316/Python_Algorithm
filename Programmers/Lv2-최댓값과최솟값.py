def solution(s):
    list_s = sorted(list(map(int, s.strip().split())))
    answer = []
    answer.append(list_s[0])
    answer.append(list_s[-1])
    
    return ' '.join(map(str, answer))