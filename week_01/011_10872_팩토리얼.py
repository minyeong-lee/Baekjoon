import sys

def solution(n):
    # N! 을 출력하는 프로그램 작성하기
    if n > 1:
        return n * solution(n-1)
    else:
        return 1

N = int(sys.stdin.readline().strip())
print(solution(N))