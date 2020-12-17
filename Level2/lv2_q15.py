# 15) 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    
    if sum(numbers) == 0: return "0"
    
    str_nums = list(map(str, numbers))
    nums = []
    
    for strn in str_nums:
        strN = strn*4
        nums.append([int(strN[0:4]), int(strn)])
    nums = sorted(nums, key=lambda x : (-x[0], x[1]))

    for n in nums:
        answer += str(n[1])
    return answer