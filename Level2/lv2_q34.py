# 34) 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []

    tmp_spell = ''
    
    for i, w in enumerate(words):
        if i != 0 : 
            if w[0] != tmp_spell or words[0:i].count(w) > 0:
                answer = [(i % n) + 1, i//n + 1]
                return answer
        tmp_spell = w[-1] #앞 단어의 가장 마지막 글자 저장
    else : return [0,0]