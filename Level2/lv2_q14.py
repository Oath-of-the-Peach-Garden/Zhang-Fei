# 14) 주식 가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    
    size = len(prices)
    for i, p in enumerate(prices):
        if p == 1: # 1이면 더 떨어질 일이 없으므로 남은 인덱스의 길이동안 가격이 떨어지지않음
            answer.append(size-(i+1))
        else: # 1이 아니라면 떨어질 여지가 있으므로, p보다 작은 값을 만나면 인덱스의 길이를 계산함
            for j in range(i+1, size):
                next_p = prices[j] #현재 가격보다 뒤의 인덱스를 조사
                if p > next_p:
                    answer.append(j-i)
                    break #적은 값이 들어오면 append하고 break
            else: #만약 if를 타지않고 끝까지 for문을 돌 경우
                answer.append(size-(i+1))
            
    return answer