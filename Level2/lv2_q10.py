# 10) 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []

    for i, a1 in enumerate(arr1):
        tmp_arr = []
        
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr2)):
                a = a1[k]
                # print('a', a)
                b = arr2[k][j]
                # print('b', b)
                tmp += a*b
            tmp_arr.append(tmp)
            # print(tmp_arr)
        answer.append(tmp_arr)
    return answer