import sys
read = sys.stdin.readline

N, K = map(int, read().strip().split())

INPUT = list(read().strip())
result = 0

for i in range(N):
    if INPUT[i] == 'P':
        for j in range(max(i-K,0), min(i+K+1, N)):
            if INPUT[j] == 'H':
                INPUT[j] == 0
                result += 1
                break
            
print(result)