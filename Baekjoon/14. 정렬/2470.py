# 산성 1~10억 알칼리 -1~-10억
# 합쳐서 0에 가까운 용액 만들려함
import sys
read = sys.stdin.readline

n = int(read())
liquids = list(map(int, read().split()))
liquids.sort()

left = 0
right = n-1

answer = abs(liquids[left] + liquids[right])
result = [liquids[left], liquids[right]]

while left < right:
    left_val = liquids[left]
    right_val = liquids[right]
    
    sum = left_val + right_val
    
    if abs(sum) < answer:
        answer = abs(sum)
        result = [liquids[left], liquids[right]]
        
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1
        
print(result[0], result[1])