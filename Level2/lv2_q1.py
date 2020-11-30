# 1) 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    
    answer = ''
    
    remain = ''
    while n > 0:
        r = 0
        if n % 3 == 0: #3의 배수이면
            r = (n-1) % 3 + 1
            n = (n-1) // 3
        else: #3의 배수가 아니면
            r = n % 3
            n = n // 3
        remain += str(r)
    remain = remain[::-1]
    
    answer = remain.replace("3", "4")
    print(answer)
    
    return answer