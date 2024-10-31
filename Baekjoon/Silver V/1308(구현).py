from datetime import *

today = list(map(int, input().split()))
d_day = list(map(int, input().split()))

if today[0] + 1000 < d_day[0]:
    print("gg")
elif today[0] + 1000 == d_day[0] and (today[1], today[2]) <= (d_day[1], d_day[2]):
    print("gg")
else:
    today = datetime(year=today[0], month=today[1], day=today[2])
    d_day = datetime(year=d_day[0], month=d_day[1], day=d_day[2])
    
    print("D-" + str((d_day-today).days))