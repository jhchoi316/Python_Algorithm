import sys
import math
read = sys.stdin.readline

M = int(read())
pebbles = list(map(int, read().split()))
K = int(read())
N = sum(pebbles)

total = math.comb(N, K)
same_colour = 0

for p in pebbles:
    same_colour += math.comb(p, K)

print(same_colour/total)