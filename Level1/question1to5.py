

# 4번) 
# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    
    dolls = []
    
    for m in moves:
        i = 0
        while i<len(board):
            tmp = board[i][m-1]
            if tmp == 0:
                i += 1
            else:
                dolls.append(tmp)   
                board[i][m-1] = 0
                break
        if len(dolls) >= 2 :
            if dolls[-1] == dolls[-2]:
                dolls = dolls[0:-2]
                answer += 2
    return answer