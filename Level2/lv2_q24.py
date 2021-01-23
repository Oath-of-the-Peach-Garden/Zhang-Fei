# 24) 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(prog, speeds):
    answer = []
    
    while prog: #있는 동안
        days = math.ceil((100 - prog[0]) / speeds[0])
        
        tmp_cnt = 0
        
        for i, (p, s) in enumerate(zip(prog, speeds)):
            prog[i] = p + (s*days)
        
        while prog:
            if prog[0] < 100: break
            prog.pop(0)
            speeds.pop(0)
            tmp_cnt += 1
            
        answer.append(tmp_cnt)
        
    return answer