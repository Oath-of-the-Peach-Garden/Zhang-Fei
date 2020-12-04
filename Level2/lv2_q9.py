# 9) 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
        
    pibo = [0 for i in range(n+1)]
    pibo[0] = 0
    pibo[1] = 1
    
    for i in range(2, n+1):
        tmp_pibo = pibo[i-1] + pibo[i-2]
        pibo[i] = tmp_pibo
    
    answer = pibo[n] % 1234567
    
    return answer