n, m = map(int, input().split())

eggs = [int(input()) for _ in range(m)]

eggs = list(sorted(eggs))

for i in range(m-1):
    if eggs[i]*2 > eggs[i+1]:
        if n < m-i:
            print(eggs[i], n * eggs[i])
            break
        else:
            print(eggs[i], (m-i) * eggs[i])
            break


# 2 7 8 10
# 2 2 <= 7
# 7 7 > 8

# 1 2 3 6
# 1 1 <= 2
# 2 2 > 3

# 1 2 5 9
# 1 1 <= 2
# 2 2 <= 5
# 5 5 > 9