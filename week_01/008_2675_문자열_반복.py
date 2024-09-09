import sys

def solution(T, tests):    
    # tests = ['3 ABC', '5 /HTP']
    # 각 요소를 꺼내서 공백을 기준으로 자른다 => 완료!
    # 자른 것 중 문자열을 한 글자씩 잘라서, 각 요소를 해당 번수로 반복해서 출력한다
    # 이 모든 걸 tests의 원소 개수만큼, 즉 T만큼 한다
    
    answer = []
    iter_str = []
    for i in range(T):
        [it, ch] = tests[i].split(' ')  # [it, ch] = ['3', 'ABC']
        print('여기서의 ch는 : ', ch)
        it = int(it)
        box = []
        for x in ch:
            char = (x * it)
            box.append(char)
        answer.append(box)
        
        print(answer)
    
    print(answer)  
    

    
T = int(sys.stdin.readline().strip())
tests = []
for i in range(T):
    R = sys.stdin.readline().strip()
    tests.append(R)
print(solution(T, tests))


