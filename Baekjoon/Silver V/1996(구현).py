N = int(input())
ground = []
answer = [[] for _ in range(N)]
nearGround = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(N):
    ground.append(list(input()))

for i in range(N):
    for j in range(N):
        if ground[i][j] != ".":
            answer[i].append("*")
        else:
            count = 0
            for k in nearGround:
                if ((i + k[0]) >= 0 and
                    (j + k[1]) >= 0 and
                    (i + k[0]) <= (N-1) and
                    (j + k[1]) <= (N-1) and
                        ground[i + k[0]][j + k[1]] != "."):
                    count += int(ground[i + k[0]][j + k[1]])
            if count > 9:
                count = "M"
            answer[i].append(str(count))

for i in answer:
    print(*i, sep='')