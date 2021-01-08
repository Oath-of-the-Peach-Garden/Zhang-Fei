# 27) 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

import itertools
def solution(numbers, target):
    answer = 0
    
    nums = [(-n, n) for n in numbers]
    
    prod_sum = list(map(sum, itertools.product(*nums)))
    answer = prod_sum.count(target)
    
    return answer