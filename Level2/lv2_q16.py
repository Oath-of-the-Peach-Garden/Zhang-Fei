# 16) H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    
    sorted_c = sorted(citations, reverse=True)
    print(sorted_c)
    
    for i, c in enumerate(sorted_c):
        answer = i+1
        if answer > c:
            return answer-1
    else:
        answer = len(citations)
    
    return answer