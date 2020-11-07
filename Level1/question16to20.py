# 16) 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915
# 20분 고민하고 아닌것같아서 다른방법 모색
# 1트
# def solution_16(strings, n):
#     answer = []
#     dict_s = {}
#     set_answer = {}
    
#     for s in strings:
#         dict_s[s] = s[n]
        
#     d_values = list(dict_s.values())
#     d_values.sort()
#     # print(d_values)
    
#     for d in d_values:
#         for k, v in dict_s.items():
#             if d == v:
#                 answer.append(k)
#                 set_answer = set(answer)
#     # print(set_answer)
#     return list(set_answer)

# 2트
# index로 뽑아낸 값을 문자열의 맨 앞에다 붙인 후, 정렬
# 그것을 문자열slice 해서 1번째index부터 맨 끝까지 출력해내면 됨 
def solution_16():
    strings = ['abce', 'abcd', 'cdx']
    n = 2
    answer = []
    tmp = []
    
    index_s = ''
    
    for s in strings:
        index_s = s[n]
        s = index_s + s
        tmp.append(s)
    tmp.sort()
        
    for t in tmp:
        answer.append(t[1:])
    print(answer)
    return answer



# 18) 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917
def solution_18(s):
    answer = ''
    temp = []
    
    #아스키의 역순
    temp = list(map(ord,s))
    temp.sort(reverse=True)
    
    temp = list(map(chr,temp))
    answer = ''.join(temp)
    return answer


# 19) 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution_19(s):
    answer = True
    
    #일단 길이가 4 또는 6일때
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if not 47 < ord(s[i]) < 58:
                return False
                break
    else:
        answer = False
        
    return answer
