import sys
read = sys.stdin.readline
n = int(read())

arr = [int(read()) for _ in range(n)]

arr.sort()

# 산술평균
print(round(sum(arr)/n))
# 중앙값
print(arr[len(arr)//2])
# 최빈값
dict = {}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

mx = max(dict.values())
mx_dict=[]

for i in dict:
    if mx==dict[i]:
        mx_dict.append(i)

if len(mx_dict)>1:#
    print(mx_dict[1])
else:#하나라면
    print(mx_dict[0])

# 범위값
print(max(arr)-min(arr))