# 23) 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587


def solution(pri, location):
    
    que = [(i,p) for i,p in enumerate(pri)]
    print(que)

    answer = 0
    while True:
        tmp = que.pop(0)
        if any(tmp[1] < q[1] for q in que):
            que.append(tmp)
        else:
            answer += 1
            if tmp[0] == location:
                return answer