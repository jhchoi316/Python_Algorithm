import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
result = []

for _ in range(n):
    flag = False
    word = deque(read().rstrip())
    
    for w in result:
        if ''.join(list(word)) in w:
            flag = True
            break
            
    if flag:
        continue
    
    words = []
    for _ in range(len(word)):
        word.rotate(1)
        words.append(''.join(list(word)))
    result.append(words)

print(len(result))