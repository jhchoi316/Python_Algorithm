polyonomio = list(input())
result = []
tmp = []

for i in range(len(polyonomio)):
    
    if polyonomio[i] == 'X':
        tmp.append(polyonomio[i])
        continue
    
    else:
        # 2로 나누어지지 않으면
        if len(tmp)%2 != 0:
            print('-1')
            exit(0)
            
        # 2로 나누어 지면
        else:
            # 4로 나누어 지면
            if len(tmp)%4 == 0:
                result.append("AAAA" * (len(tmp)//4))
            # 4로 나누어지지 않지만 2로 나누어 지면
            else:
                if len(tmp)%2 == 0:
                    result.append("AAAA" * (len(tmp)//4))
                    result.append("B" * (len(tmp)%4))
        tmp = []
        result.append(".")

# 2로 나누어지지 않으면
if len(tmp)%2 != 0:
    print('-1')
    exit(0)
            
# 2로 나누어 지면
else:
# 4로 나누어 지면
    if len(tmp)%4 == 0:
        result.append("AAAA" * (len(tmp)//4))
    # 4로 나누어지지 않지만 2로 나누어 지면
    else:
        if len(tmp)%2 == 0:
            result.append("AAAA" * (len(tmp)//4))
            result.append("B" * (len(tmp)%4))

print(''.join(map(str,result)))