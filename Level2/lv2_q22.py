# 22) 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
                
    for tmp in phone_book:
        for nxt in phone_book:
            if tmp==nxt or len(tmp) > len(nxt):continue
            else:
                if tmp == nxt[:len(tmp)]:
                    return False
    return answer