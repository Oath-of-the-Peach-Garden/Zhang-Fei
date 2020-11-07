

# 9) 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901
def solution_9():
    #숫자는 테스트용으로 넣음
    a = 5
    b = 24

    answer = ''

    #1~12월까지의 날짜가 0~11의 인덱스에 담겨있음
    months = [31,29,31,30,31,30,31,31,30,31,30,31]

    days = 0 #1월 1일부터 센 총 일수
    remain = 0

    for i in range(a-1):
        days += months[i]
    days += b
    print(days)

    dow = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    remain = days % 7 
    answer = dow[remain]

    return answer


# 10) 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution_10():
    s = 'ABCDE'
    answer = ''
    
    size = len(s)
    center = int(size/2)
    if size % 2 == 0: #글자수가 짝수라면
        answer = s[center-1 : center+1]
    else: #홀수라면
        answer = s[center]
    return answer


