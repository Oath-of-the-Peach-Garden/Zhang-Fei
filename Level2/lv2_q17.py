# 17) 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    
    answer = 0
    nlist = list(name)
    for n in nlist:
        #위아래 이동 카운트
        if n != 'A': #A가 아닐때만 카운트 해야하니까
            up = ord(n) - ord('A')
            down = ord('Z') - ord(n) + 1 
            answer += min(up, down)
            # print('-----------answer : ', answer)
        
    index = 0
    while True: 
        left = right = 1 #왼쪽, 오른쪽으로 이동한 칸 수
        nlist[index] = 'A'
        if all(n == 'A' for n in nlist): break #모두 A가 됐으면 탈출
        
        while nlist[index+right] == 'A': # 이동했는데 A라면 한칸 더 이동(A가 아닌게 나올때까지)
            right += 1
        while nlist[index-left] == 'A': #이동했는데 A라면 한칸 더 이동(A가 아닌게 나올때까지)
            left += 1
            
        answer += left if left < right else right #answer에 이동한 횟수만큼을 더함
        index += -left if left < right else right #현재위치(index)를 조정해줌
    return answer