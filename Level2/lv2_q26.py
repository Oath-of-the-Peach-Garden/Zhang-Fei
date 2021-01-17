# 26) 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    cdict = {}
    for cloth, cate in clothes:
        if cate not in cdict:
            cdict[cate] = 1
        else:
            cdict[cate] += 1
    cvalues = cdict.values()
    for cv in cvalues:
        answer *= (cv+1)
    return answer-1