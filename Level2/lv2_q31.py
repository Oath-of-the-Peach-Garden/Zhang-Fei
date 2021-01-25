# 31) 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    step = list(skill)
    
    for skill in skill_trees:
        copy_step = step[:]
        for s in skill:
            if s in copy_step and s != copy_step.pop(0):
                break
        else:
            answer += 1
        print(answer)
    return answer