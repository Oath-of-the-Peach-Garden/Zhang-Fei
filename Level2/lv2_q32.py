# 32) 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

import itertools
def solution(nums):
    answer = 0
    
    nums.sort(reverse=True)
    maxi = sum(nums[0:3])
    
    che = [0] * (maxi+1)
    for i, c in enumerate(che):
        if i == 0 or i == 1: che[i] = 1 #소수가 아님
        else:
            for j in range(i*2, maxi+1, i):
                che[j] = 1
    
    hap_list = list(map(sum, itertools.combinations(nums, 3)))
    
    for hap in hap_list:
        if che[hap] == 0:
            answer += 1

    return answer