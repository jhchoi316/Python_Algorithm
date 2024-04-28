T = int(input())

for i in range(T):
    N = int(input())
    cnt0, cnt1 = 1, 0
    for j in range(N):
        cnt0, cnt1 = cnt1, cnt0+cnt1

print(cnt0, cnt1)