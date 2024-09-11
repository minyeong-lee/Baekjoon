from itertools import combinations
import sys

def solution(nums):
    # print('nums는요', nums) #['20', '7', '23', '19', '10', '15', '25', '8', '13']
    # cnt_list = []
    # if len(cnt_list) == 7:
        # 7개의 원소 합이 100인지 확인하기
        
        # 만약 7개 원소의 합이 100이라면 return
    
    for comb in combinations(nums, 7):
        comb = list(comb)
        if sum(comb) == 100:
            comb = sorted(comb)
            return '\n'.join(map(str, comb))

nums = []
for i in range(9):
    nums.append(int(sys.stdin.readline().strip()))
print(solution(nums))

# DFS의 기본 원칙
# DFS에서 데이터를 찾을 때는 '앞으로 찾아 가야할 노드'와 '이미 방문한 노드'를 기준으로 데이터를 탐색한다
# 특정 노드가 '앞으로 찾아 가야할 노드'이면 계속 검색하고, '이미 방문한 노드'이면 무시하거나 따로 저장하기

"""
의사 코드 (Pseudocode)

def DFS(난쟁이 수, 합계):
    if 난쟁이 수 == 7: # 7명을 다 선택했으면
        if 합계 == 100: # 키 합이 100이면
            # 정답 출력 후 종료
        return
    
    for i in range(9):
        if 방문한 난쟁이[i]:  # 이미 선택한 난쟁이는 건너뜀
            continue
        
        방문한 난쟁이[i] = True # 난쟁이를 선택함
        DFS(난쟁이 수 + 1, 합계 + i번째 난쟁이 키)  # 다음 난쟁이를 선택하러 감
        방문한 난쟁이[i] = False  # 백트래킹: 선택을 취소함
        
"""