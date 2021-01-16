# 33) 점프와 순간이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 1: #홀수라면
            n -= 1
            ans += 1
        else:
            n //= 2

    return ans