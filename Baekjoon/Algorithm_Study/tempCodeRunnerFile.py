

for member in all_possible:
    first_team = 0
    second_team = 0
    
    for i in range(total_member):
        for j in range(total_member):
            if i in member and j in member:
                first_team += ability[i][j]
            else:
                second_team += ability[i][j]
    answer.append(abs(first_team - second_team))

print(min(answer))
