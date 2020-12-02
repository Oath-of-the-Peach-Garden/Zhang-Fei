# 12) JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    
    if len(s) == 1: #한글자라면 대문자로 변경하여 리턴
        return s.upper()
    
    flag = False
    #두글자 이상이라면
    for char in s:
        
        # print('char--------------',char)
        if not flag: #단어의 맨 첫 글자
            answer += char.upper()
            flag = True #플래그 뒤집어줌
        else:
            answer += char.lower() #소문자로 붙여줌
            
        if char == ' ': #현재 글자가 띄워쓰기라면 플래그 뒤집음
            flag = False
            
        # print(answer)
    return answer