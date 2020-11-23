

# 48) 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    
    d.sort() #오름차순 정렬
    hap = 0
    for i, v in enumerate(d):
        hap += v
        if hap > budget:
            return i
    return i+1