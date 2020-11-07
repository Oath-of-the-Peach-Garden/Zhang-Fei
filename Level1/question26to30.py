




# 27) 이상한 숫자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

#1트
# def solution_27():
#     answer = ''
#     result = []

#     s = '  python  hello  world'

#     words_arr = s.split(' ')  #["try", "hello", "world"] 로 잘라서 배열에 넣기
#     print(words_arr)
#     for word in words_arr:
#         for i in range(len(word)):
#             w = list(word)
#             if i % 2 == 0:  #짝수
#                 w[i] = w[i].upper()
#                 result.append(w[i])
#             else:  #홀수
#                 w[i] = w[i].lower()
#                 result.append(w[i])
#         result.append(" ")

#     answer = answer.join(result).strip()
#     print(answer)
#     return answer

#2트 (7분)
def solution_27():
    s = '   python  hello world'
    answer = ''
    s_arr = list(s)

    index = 0
    
    #공백이 아닌 단어를 만나면 거기서부터 인덱스를 세기로
    for i in range(len(s_arr)):
        tmp_s = s_arr[i]
        if tmp_s == " ": #공백인 경우
            index = 0
        else: #공백이 아닌 경우
            if index % 2 == 0: #짝수
                s_arr[i] = tmp_s.upper()
            else:
                s_arr[i] = tmp_s.lower()
            index += 1
    print(s_arr)
    answer = answer.join(s_arr)
    print(answer)
    return answer

