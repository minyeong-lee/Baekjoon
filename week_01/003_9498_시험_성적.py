def solution(score):
    if 90 <= score <= 100:
        score = 'A'
    elif 80 <= score <= 89:
        score = 'B'
    elif 70 <= score <= 79:
        score = 'C'
    elif 60 <= score <= 69:
        score = 'D'
    else:
        score = 'F'
    return score


n = int(input())
print(solution(n))
