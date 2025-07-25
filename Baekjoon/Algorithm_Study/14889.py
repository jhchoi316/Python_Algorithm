import sys
read = sys.stdin.readline
from itertools import combinations

N = int(read())
members = [i for i in range(N)]
ability = [list(map(int, read().split())) for _ in range(N)]
total_member = N//2
all_possible = list(combinations(members, total_member))
answer = []

for member in all_possible:
    first_team = 0
    second_team = 0

    for i in range(N):
        for j in range(N):
            if i in member and j in member:
                first_team += ability[i][j]
            else:
                second_team += ability[i][j]
        print(first_team)
    answer.append(abs(first_team - second_team))
print(all_possible)
print(answer)
print(min(answer))
