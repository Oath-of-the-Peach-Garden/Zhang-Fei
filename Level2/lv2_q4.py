# 4) 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0

    n_cnt = bin(n).count('1')
    
    while 1:
        n += 1
        tmp_cnt = bin(n).count('1')
        if tmp_cnt == n_cnt:
            answer = n
            break
    
    return answer