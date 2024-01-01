# 수학여행 참가 인원, 최대 방 인원
# 같은 학년, 같은 성별
# 여자 0 남자 1

total_num, total_room_num = map(int,input().split(" "))

female_member = []
male_member = []

for i in range(total_num):
    member = list(map(int,input().split(" ")))
    if member[0] == 0:
        female_member.append(member[1])
    else:
        male_member.append(member[1])

female_member.sort(), male_member.sort()

room_count = 0

for i in range(1,7): 
    
    if (female_member.count(i)) != 0 and  (female_member.count(i) <= total_room_num):
        room_count += 1
    elif (female_member.count(i) > total_room_num) and (female_member.count(i) % total_room_num) == 0:
        room_count += int(female_member.count(i) / total_room_num)
    elif (female_member.count(i) > total_room_num) and (female_member.count(i) % total_room_num) != 0:
        room_count += int(female_member.count(i) / total_room_num) + 1      

    if (male_member.count(i) != 0) and (male_member.count(i) <= total_room_num) :
        room_count += 1
    elif (male_member.count(i) > total_room_num) and (male_member.count(i) % total_room_num == 0):
        room_count += int(male_member.count(i) / total_room_num)
    elif (male_member.count(i) > total_room_num) and (male_member.count(i) % total_room_num != 0):
        room_count += int(male_member.count(i) / total_room_num) + 1   

print(room_count)
