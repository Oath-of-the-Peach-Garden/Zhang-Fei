# 25) 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville) #작은 수 부터 정렬
    
    while len(scoville) > 1:
        newnum = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, newnum)
        answer+=1
        if scoville[0] >= k:
            return answer
        elif len(scoville) == 1:
            return -1
        
    return answer