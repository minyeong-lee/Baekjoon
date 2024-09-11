import sys

def solution(n, nums):
    nums.sort()
    for x in nums:
        print(x)
        
N = int(sys.stdin.readline().strip())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline().strip()))
solution(N, nums)