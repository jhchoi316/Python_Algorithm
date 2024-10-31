n = int(input())

students = [[0]*n for i in range(n)]
data = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(5):
        for k in range(n):
            if data[i][j] == data[k][j]:
                students[i][k] = 1

answers = [0] * n

for i, student in enumerate(students):
    answers[i] = student.count(1)

for i in range(n):
    if answers[i] == max(answers):
        print(i+1)
        break