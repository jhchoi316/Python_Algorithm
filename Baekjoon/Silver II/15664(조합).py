import sys
from itertools import combinations
read = sys.stdin.readline

N, M = map(int, read().split())
N_list = list(map(int, read().split()))
N_list = sorted(N_list)
output = []

for numbers in list(combinations(N_list, M)):
    if not output:
        output.append(numbers)
    elif numbers not in output:
        output.append(numbers)
            
for numbers in output:
    for num in numbers:
        print(num, end=' ')
    print()