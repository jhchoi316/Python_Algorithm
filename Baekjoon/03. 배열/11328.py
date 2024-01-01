
for i in range(int(input())):
    str1, str2 = map(sorted, list(input().split(" ")))
    if str1 == str2:
        print("Possible")
    else:
        print("Impossible")