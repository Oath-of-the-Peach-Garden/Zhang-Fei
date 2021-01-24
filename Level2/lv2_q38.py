# 38) 예상대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0
    
    def div(n):
        if n % 2 == 0:
            n //= 2
        else:
            n = n//2 +1
        return n
    
    while a != b:
        a = div(a)
        b = div(b)
        
        answer += 1
        
    return answer