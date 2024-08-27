S = list(map(int,input()))

cnt0 = 0
cnt1 = 0

for i in range(1,len(S)):
    if S[i] == 1 and S[i-1] == 1:
        continue
    elif S[i] == 0 and S[i-1] == 1:
        cnt1 += 1
    elif S[i] == 0 and S[i-1] == 0:
        continue
    elif S[i] == 1 and S[i-1] == 0:
        cnt0 += 1
        

if cnt0 > cnt1:
    print(cnt0)
else:
    print(cnt1)