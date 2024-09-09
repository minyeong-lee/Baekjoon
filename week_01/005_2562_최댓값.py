import sys

def solution(nums):
    max_v = 0
    max_idx = 0
    for i in range(len(nums)):
        if nums[i] > max_v:
            max_v = nums[i]
            max_idx = i + 1
    return max_v, max_idx

nums = []
for i in range(9):
    nums.append(int(sys.stdin.readline().strip()))
x, y = solution(nums)
print(x)
print(y)