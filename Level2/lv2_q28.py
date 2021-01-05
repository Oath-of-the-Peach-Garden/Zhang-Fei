# 28) 삼각달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645


def solution(n):
    answer = []
    
    tmp_list = [[0 for _ in range(n)] for _ in range(n)]
    
    x = 0 #가로
    y = -1 #세로
    
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: y += 1 #밑으로 이동
            elif i % 3 == 1: x += 1 #오른쪽 이동
            elif i % 3 == 2: #왼쪽 위 대각선 이동
                x -= 1
                y -= 1
            tmp_list[y][x] = num #좌표에 숫자를 입력
            num += 1
    
    for tmp in tmp_list:
        for t in tmp:
            if t != 0:
                answer.append(t)
    
    return answer