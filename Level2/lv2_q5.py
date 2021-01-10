# 5) 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0
    
    if len(land) == 1: #한줄짜리 땅이라면
        return max(land[0])
    
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            prev_line = land[i-1][:]
            del prev_line[j]
            land[i][j] = land[i][j] + max(prev_line)
    answer = max(land[-1])
    return answer