import sys
read = sys.stdin.readline

while True:
    try:
        N = int(read())
    except:
        break

    result = 1
    index = 1
    
    while True:
        if result%N == 0:
            print(len(str(result).strip()))
            break
        else:
            result += (10**index)
            index += 1