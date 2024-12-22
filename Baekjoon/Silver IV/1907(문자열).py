import sys
read = sys.stdin.readline

left, right = read().strip().split("=")
left0, left1 = left.split("+")

cnt = {'C':0, 'H':1, 'O':2}

def count(x):
    result = [0]*3
    before = None
    
    for i in x:
        if i in ['C', 'H', 'O']:
            result[cnt[i]] += 1
            before = i
        else:
            result[cnt[before]] += int(i)-1
    return result

x, y, z = count(left0), count(left1), count(right)

answer = []
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            if x[0]*i + y[0]*j == z[0]*k and \
                x[1]*i + y[1]*j == z[1]*k and \
                x[2]*i + y[2]*j == z[2]*k:
                        answer.append([i,j,k])

print(*answer[0])