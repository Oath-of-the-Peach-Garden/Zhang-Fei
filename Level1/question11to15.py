
# 12) 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution_12(arr):
    answer = []
    size = len(arr)
    for i in range(size-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer


# 14) 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution_14(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    if len(answer) == 0:
        answer.append(-1)
        
    answer.sort()
    return answer

# 15) 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution_15(a, b):
    answer = 0
    for i in range(min(a,b), max(a,b)+1):
        answer += i
    return answer