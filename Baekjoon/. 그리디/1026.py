N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort(reverse=True)

res = 0
for i in range(N):
    res += arr1[i]*arr2[i]

print(res)