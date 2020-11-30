# 7) 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    
    s_list = list(map(int, s.split())) 
    
    answer += str(min(s_list)) + ' '
    answer += str(max(s_list))
    return answer