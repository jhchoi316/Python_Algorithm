import sys
import collections
read = sys.stdin.readline

n = list(read().rstrip())
check_word = collections.Counter(n)
count = 0
result = ''
mid = ''

for k, v in list(check_word.items()):
    if v % 2 == 1:
        count+=1
        mid = k
        if count >= 2:
            print("I'm Sorry Hansoo")
            exit()
            
for k, v in sorted(check_word.items()):
    result += (k * (v // 2))

print(result + mid + result[::-1])