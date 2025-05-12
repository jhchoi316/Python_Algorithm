def check_alphabet(c):
    if c.islower():
        return True
    elif c.isupper():
        return False

def convert(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()
    
def solution(s):
    answer = ''
    index = 0
    
    for i in range(len(s)):
        if index == 0 and s[i] != " ":
            if check_alphabet(s[i]):
                answer += convert(s[i])
            else: answer += s[i]
            index += 1
            
        elif index != 0 and s[i] != " ":
            if not check_alphabet(s[i]):
                answer += convert(s[i])
            else: answer += s[i]
            index += 1
        
        elif s[i] == " ":
            answer += s[i]
            index = 0
    
    return answer