T = int(input())

for i in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    res = 0
    maxPrice = 0
    for j in range(len(price)-1, -1, -1):
        if price[j] > maxPrice:
            maxPrice = price[j]
        else:
            res += maxPrice - price[j]

    print(res)