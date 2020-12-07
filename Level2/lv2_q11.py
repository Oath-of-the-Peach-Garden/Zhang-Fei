# 11) N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

import math

def solution(arr):
    answer = 0
    
    # a*b = gcd * lcm
    # 파이썬은 gcd를 제공해주는걸 또 까먹었다
    
    lcmarr= [1]
    
    for i in range(len(arr)):
        num1 = lcmarr[i]
        num2 = arr[i]
        print(num1, num2)
        tmp = num1*num2 // math.gcd(num1, num2)
        
        lcmarr.append(tmp)
        
    answer = lcmarr[-1]
    return answer