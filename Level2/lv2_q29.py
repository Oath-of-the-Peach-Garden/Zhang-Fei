# 29) 쿼드압축 후 개수 세기
# https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]

    def check_num(x, y, size, arr):
        # print('------------------',x,y,size)
        zero = 0
        one = 0
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[j][i] == 0: zero+=1
                else: one +=1
        if zero == 0: #전부 1이면
            answer[1] += 1 
            return
        elif one == 0: #전부 0이면
            answer[0] += 1 
            return
        
        half = size//2
        check_num(x, y, half, arr)
        check_num(x+half, y, half, arr)
        check_num(x, y+half, half, arr)
        check_num(x+half, y+half, half, arr)
    
    check_num(0, 0, len(arr), arr)
            
    return answer