# 51) [1차] 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution51(dartResult):
    answer = 0
    
    jum = 0
    jums = []
    
    asciiA = ord('A')
    asciiZ = ord('Z')
    
    cnt = -1 #다트를 던진 횟수
    
    s = 0
    for i, d in enumerate(dartResult):
        # print('---------------------i :',i,'/ d :',d)
        if asciiA <= ord(d) <= asciiZ : #알파벳이 나오면
            jum = int(dartResult[s:i])
            s = i+1
            # print('jum :',jum, ', 보너스 :', d)
            
            if d == 'D':
                jum = jum ** 2
            elif d == 'T':
                jum = jum ** 3
            # print ('수정된 jum : ', jum)
            jums.append(jum)
            cnt += 1
        
        if d == '*':
            # print('*에 당첨')
            s += 1
            if len(jums) > 1: #점수가 2개 이상이면
                jums[cnt-1] = jums[cnt-1] * 2
                jums[cnt] = jums[cnt] * 2
            else : #점수가 하나 뿐이면
                jums[cnt] = jums[cnt] * 2
                
        if d == '#':
            # print('저런! #에 당첨')
            s += 1
            jums[cnt] = jums[cnt] * -1
        # print(jums)
    answer = sum(jums)
    return answer