def solution(n, words):
    answer = [0,0]
    previous_alpha = words[0][-1]
    dict_words = {}
    dict_words[words[0]] = 1
    
    for i in range(1, len(words)):
        if words[i] in dict_words:
            dict_words[words[i]] += 1
        else:
            dict_words[words[i]] = 1
            
        if words[i][0] == previous_alpha and dict_words[words[i]] == 1:
            previous_alpha = words[i][-1]
            
        else:
            answer = [(i%n)+1,(i//n)+1]
            break
            
    return answer