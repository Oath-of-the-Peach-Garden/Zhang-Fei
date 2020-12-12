# 2) 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0
    
    if len(board) == 1 or len(board[0]) == 1: #board의 크기가 1*n 또는 n*1 이라면
        hap = 0
        for b in board:
            hap += sum(b)
        if hap > 0: return 1
        else: return 0
    
    tmp = 0
    for i in range(1, len(board)):
        # print('--------------------------------')
        for j in range(1, len(board[i])):
            tmp_room = board[i][j]
            # print(tmp_room)
            if tmp_room == 1: #지금 칸이 1일때만
                chk_min = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                board[i][j] = chk_min+1
                tmp = max(tmp, chk_min+1)
                # print('chk_min', chk_min+1)

    return tmp ** 2