import sys
from collections import deque
read = sys.stdin.readline

N, D, K, C = map(int, read().strip().split())

table = []
count = 1
eaten = [0] * (D+1)
eaten[C] = 1

for i in range(N):
    table.append(int(read()))

# 처음 4개 초기화
for i in range(K):
    eaten[table[i]] += 1
    if eaten[table[i]] == 1:
        count += 1

result = count

for i in range(N-1):
    print(table[i], eaten[table[i]])

    # 가장 앞의 숫자 제거
    eaten[table[i]] -= 1
    
    # 뺀 숫자가 중복되는지 확인
    if eaten[table[i]] == 0:
        count -= 1
    
    # 다음 숫자 추가
    eaten[table[(i+K) % N]] += 1
    
    # 다음 숫자 중복되는지 확인
    if eaten[table[(i+K) % N]] == 1: 
        count += 1
    
    result = max(result, count)

print(result)