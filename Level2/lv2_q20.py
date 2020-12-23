# 20) 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0
    
    nums = list(map(int, numbers))
    nums.sort(reverse=True)
    
    #체 만드는 작업
    max_num = int("".join(str(n) for n in nums)) #체를 가장 큰 수만큼 만들기위해 생성
    nums_net = [0] * (max_num+1) #체를 만듬, 기본 0
    nums_net[1] = 1 #1은 소수가 아니니 제외해주고
    
    for i in range(2, max_num+1):
        if nums_net[i] == 0:
            for j in range(2*i, max_num+1, i):
                nums_net[j] = 1 #소수가 아닌 애들을 1로 변경
    
    #수를 조합해서 확인하는 작업 (조합은 파이썬 라이브러리 사용)
    # https://docs.python.org/ko/3/library/itertools.html#itertools.permutations
    made_nums_list = []
    for i in range(len(numbers)+1):
        # [(), (7,), (1,), (7, 1), (1, 7)]
        #이런 식으로 들어있음        
        made_nums_list += list(permutations(nums, i)) 
        
    made_nums = [] #위의 조합을 int형으로 변경해서 저장하기위한 리스트
    for i in range(len(made_nums_list)):
        tmp_num = "".join(str(n) for n in made_nums_list[i]) 
        if tmp_num != '':
            made_nums.append(int(tmp_num))
    
    made_nums = set(made_nums)
    # print(made_nums)
    
    for n in made_nums:
        if n != 0 and nums_net[n] == 0:
            answer += 1
    
    return answer