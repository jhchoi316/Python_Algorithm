n, m = map(int, input().split())
package = []
each = []
result = 0

for i in range(m):
    a, b = map(int, input().split())
    package.append(a)
    each.append(b)

min_package = min(package)

while n > 0:
    if n >= 6:
        min_each = min(each)*6
        n -= 6
    else:
        min_each = min(each)*n
        n -= n
    if min_each < min_package:
        result += min_each
    else:
        result += min_package

print(result)