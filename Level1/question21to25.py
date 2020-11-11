
# 21) 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
# 16분

def solution_21():
    answer = 0
    
    # n = int(input()) #입력받은 수
    n = 20 #테스트용

    num_list = [0]*(n+1) #0이 솟수고 1이 합성수
    
    for i in range(2, n+1):
        if num_list[i] == 1 : continue
        
        for j in range(2*i, n+1, i):
            num_list[j] = 1

    #0과 1은 솟수가 아니기 때문에, 전체 갯수를 센 후, 2를 빼줘야함
    answer = num_list.count(0)-2
    # print('answer', answer)
    
    return answer



# 24) 시저암호
# https://programmers.co.kr/learn/courses/30/lessons/12926
# 22분
def solution_24():
    #s, n은 테스트용으로 입력함
    s = 'A  Zz' 
    n = 7 #H Gg 가 나와야 함
    
    s_list = list(s)
    answer_list = []
    answer = ''
    
    # #문자열의 길이만큼
    # for i in range(len(s_list)):
    #     if s_list[i] == ' ': #공백이라면
    #         continue    #건너뜀
        
    #     ascii_s = ord(s_list[i])
    #     tmp_ascii = ascii_s + n

    #     #대문자인경우
    #     if 65 <= ascii_s <= 90 and tmp_ascii>90:
    #       tmp_ascii = tmp_ascii - 26

    #     #소문자인경우
    #     if 97 <= ascii_s <= 122 and tmp_ascii>122:
    #       tmp_ascii = tmp_ascii - 26

    #     s_list[i] = chr(tmp_ascii)
    # answer = answer.join(s_list)
    # print(answer)
    # return answer
    
    for s in s_list:
        if s == ' ':
            answer_list.append(' ')
            continue

        ascii_s = ord(s)
        ascii_A = ord('A')
        ascii_a = ord('a')
        tmp_ascii = 0

        if s.isupper(): #대문자라면
            tmp_ascii = (ascii_s - ascii_A + n) % 26 + ascii_A
        elif s.islower(): #소문자라면
            tmp_ascii = (ascii_s - ascii_a + n) % 26 + ascii_a
        answer_list.append(chr(tmp_ascii))
        
    answer = answer.join(answer_list)
    return answer