import sys
read = sys.stdin.readline

nums = read()

def solution(nums):
    set_nums = set(nums)
    # 종류가 n/2보다 적을 경우
    if len(set_nums) <= len(nums)//2:
        return len(set(nums))
    else:
        return len(nums)//2
