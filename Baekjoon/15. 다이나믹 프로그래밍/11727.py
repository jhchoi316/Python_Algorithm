n = int(input())

tiles = [0] * 1001

tiles[0] = 1
tiles[1] = 1

if n >= 2:
    for i in range(2, n+1):
        tiles[i] = (tiles[i-2]*2) + tiles[i-1]

print(tiles[n] % 10007)