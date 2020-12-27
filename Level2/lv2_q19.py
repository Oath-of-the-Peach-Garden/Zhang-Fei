# 19) 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    
    light = 0
    heavy = len(people)-1 #people의 마지막 인덱스
    two = 0
    
    while light < heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
            two += 1 #두명이서 나간 수
        heavy -= 1
                
    return len(people)-two