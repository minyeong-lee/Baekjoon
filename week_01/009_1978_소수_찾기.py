import sys
import math

def solution(N, nums):
    # 주어진 N개 중에서 소수가 몇 개인지 찾아서 출력하자
    # 배열에 들어있는 원소를 반복문을 돌려
    # 각 원소가 소수이면 answer에 1씩 더해 저장하자
    # 결과적으로 answer는 nums 라는 정수로 이루어진 배열에서의 소수 개수를 담는다

    answer = 0
    for x in nums:
        if x != 1:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    break
            else:
                answer += 1
    return answer


N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
print(solution(N, nums))