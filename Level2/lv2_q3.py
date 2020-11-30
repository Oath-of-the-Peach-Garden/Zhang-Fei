# 3) 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(input_s):
    answer = True
    
    if input_s[0] == ')':
        return False
    
    chk = 0
    for s in input_s:
        if chk <= 0:
            if s == ')': # )가 나오면 +1
                chk += 1
            else: # (가 나오면 -1
                chk -= 1
    
    if chk != 0:
        return False
    else:
        return True