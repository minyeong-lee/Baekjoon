import sys

def solution(N):
    mul = ''
    for i in range(1, 10):
        sum = N * i
        mul += (f'{N} * {i} = {sum}\n')
    
    return mul

N = int(sys.stdin.readline())
print(solution(N).strip())