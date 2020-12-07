# 6) 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    
    for i in range(n+1):
        num = 0
        #i = 0 이므로
        for j in range(i+1, n+1):
          # i+1 인 1부터 차례대로 더함
          # 더한게 딱 떨어지게 같으면 answer+=1 하고 break
          # 더한게 n보다 커지면 break해서 쓸데없이 더 돌지않도록 함
            num += j
            
            if num == n :
                answer += 1
                break
            if num > n :
                break
    return answer