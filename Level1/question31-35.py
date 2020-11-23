
# 34번) 키패드
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    
    dictN = {
        1:1, 2:1, 3:1,
        4:2, 5:2, 6:2,
        7:3, 8:3, 9:3,
        '*':4, 0:4, '#':4
    }
    
    tmpL = '*'
    tmpR = '#'
    
    for i, n in enumerate(numbers):
        
        if n in (1,4,7):
            answer+='L'
            tmpL = n
        elif n in (3,6,9):
            answer+='R'
            tmpR = n
        else :
            #거리를 계산하여 R, L을 판별해야함
            target = dictN.get(n) #2 5 8 0 중에서 눌러줘야하는 타겟
            
            #거리를 판단할 때 왼147 오369면 좌 우 움직임이 있으므로 dist +1
            if tmpL in (1,4,7, '*')  :
                distL = abs(target - dictN.get(tmpL))+1
            else :
                #근데 왼,오가 2580에 있으면 dist 더하지않아도 됨
                distL = abs(target - dictN.get(tmpL))
                
            if tmpR in (3,6,9, '#') :
                distR = abs(target - dictN.get(tmpR))+1
            else :
                distR = abs(target - dictN.get(tmpR))
            
            if distL == distR :
                answer+=hand[0].upper()
                if hand=='left':
                    tmpL = n
                if hand=='right':
                    tmpR = n
            elif distL > distR :
                answer+='R'
                tmpR = n
            elif distL < distR :
                answer+='L'
                tmpL = n
                
    return answer