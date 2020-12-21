# 21) 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    
    x,y = 0,0 #가로 세로
    
    extent = brown + yellow #넓이
    for a in range(1, extent//2):
        if extent % a == 0:
            b = extent // a
            if a + b == (brown + 4) // 2:
                answer = [a,b]
                answer.sort(reverse=True)
                return answer