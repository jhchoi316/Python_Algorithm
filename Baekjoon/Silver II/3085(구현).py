import sys
read = sys.stdin.readline

N = int(read())
candies = [list(read().strip()) for _ in range(N)]

def checkCount():
    max_count = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if candies[i][j] == candies[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(count, max_count)
            
        count = 1
        for j in range(1, N):
            if candies[j][i] == candies[j-1][i]:
                count += 1
            else:
                count = 1
            max_count = max(count, max_count)
    return max_count

result = 1
for i in range(N):
    for j in range(N-1):
        if j+1 < N and candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            result = max(result, checkCount())
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        if i+1 < N and candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            result = max(result, checkCount())
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(result)