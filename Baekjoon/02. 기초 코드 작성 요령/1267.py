n = int(input())
call_time_list = list(map(int, input().split(" ")))

def Y(call_time_list):
    sum = 0
    for i in call_time_list:
        if i % 30 >= 0:
            sum += int((i / 30) + 1)
    return int(sum * 10)
            
def M(call_time_list):
    sum = 0
    for i in call_time_list:
        if i % 60 >= 0:
            sum += int((i / 60) + 1)

    return int(sum * 15)

m = M(call_time_list)
y = Y(call_time_list)

if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
elif m > y:
    print("Y", y)