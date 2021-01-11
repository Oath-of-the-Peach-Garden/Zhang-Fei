# 18) 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    answer = ''
    
    st = []
    pcnt = 0 #pop 한 횟수
    for i in range(len(number)):
        tmp = number[i]
        if not st: #비어있으면 넣고 다음수로 넘어감
            st.append(tmp)
            continue
        
        while st and st[-1] < tmp and pcnt < k:
            st.pop()
            pcnt += 1
        st.append(tmp)
        # print(st)
            
    if pcnt < k:
        answer = ''.join(s for s in st[:-k])
    if pcnt == k:
        answer = ''.join(s for s in st)
    return answer