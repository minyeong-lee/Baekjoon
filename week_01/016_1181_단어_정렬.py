import sys
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로 정렬하자
# 단, 중복된 단어는 하나만 남기고 제거하자 (중복을 없애자)

def solution(N, letters):
    letters = list(set(letters))
    answer = sorted(letters, key = lambda x : (len(x), x))
    answer = '\n'.join(answer)
    return answer

# 입력을 받자!
N = int(sys.stdin.readline().strip())
letters = []
for i in range(N):
    letters.append(sys.stdin.readline().strip())

print(solution(N, letters))
