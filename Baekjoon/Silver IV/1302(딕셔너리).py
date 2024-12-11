import sys
read = sys.stdin.readline

n = int(read())

book_list = {}

for i in range(n):
    a = read()
    
    if a in book_list.keys():
        book_list[a] += 1
    else:
        book_list[a] = 1

max_value = max(book_list.values())
result = []

for key, value in book_list.items():
    if value == max_value:
        result.append(key)

result = sorted(result)
print(result[0])