import sys
read = sys.stdin.readline

N, L = map(int, read().strip().split())
leaking = sorted(list(map(int, read().strip().split())))
check = [False * N]
cover = [[0.5, leaking[0]+L-0.5]]

for i in range(1,N):
    if cover[-1][0] <= leaking[i] and leaking[i] <= cover[-1][1]:
        continue
    else:
        cover.append([leaking[i]-0.5, leaking[i]+L-0.5])
print(len(cover))