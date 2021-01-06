# 30) 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []

    zero_cnt = 0 #삭제한 0 갯수
    progress = 0 #변환 한 횟수
    
    while len(s) > 1:
        zero_cnt += s.count('0') #삭제한 0의 갯수
        
        slist = list(s) #리스트를 돌면서 1이면 붙임 (0이면 버림)
        tmps = ''
        for s in slist:
            if s == '1': tmps += s
            
        s = str(bin(len(tmps))[2:]) # 그 길이만큼 이진수로 만듬
        progress += 1 #변환한 횟수 올려줌
    answer = [progress, zero_cnt]
    return answer