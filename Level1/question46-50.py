

# 48) 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution48(d, budget):
    d.sort() #오름차순 정렬
    hap = 0
    for i, v in enumerate(d):
        hap += v
        if hap > budget:
            return i
    return i+1



# 50) 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution50(N, stages):
    answer = []
    dictN = {}
    
    # print(stages)
    ans = 0 #현재 그 단계를 통과 못한 사람(도달했으나 실패자)
    people = len(stages) #남은 사람들
    
    i = 1 #단계 카운트 하려고    
    while i < N+1:
        ans = stages.count(i)
        
        # print('i :', i, '-----ans / people', ans,'/',people)
        
        if ans == 0: #실패자가 없다는 뜻이므로 실패율이 0
            fail_rate = 0
        elif people == 0: #아예 그 단계에 도달한 사람이 없다면
            fail_rate = 0 #문제에서 0으로 정의한다고 했으므로 실패율 = 0
        else:
            fail_rate = ans/people

        dictN[i] = fail_rate
        i += 1
        people = people - ans
    # print(dictN.items())
    
    newDict = sorted(dictN.items(), key = lambda x : x[1], reverse=True) #value값으로 내림차순 정렬
    # print(newDict)
    
    answer = [newDict[i][0] for i in range(len(newDict))]
    # print(answer)
    
    return answer