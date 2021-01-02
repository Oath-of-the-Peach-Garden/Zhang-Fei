# 13) 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    time = 0

    on_truck = [0] * bridge_length
    tmp_weight = 0
    
    while on_truck:
        # print('-----------------------------------')
        time += 1
        tmp_weight -= on_truck.pop()
        # print('time, tmp_weight', time,tmp_weight)
        
        if truck_weights:
            if tmp_weight + truck_weights[0] <= weight: #무게를 넘지 않는다면
                tmp_weight += truck_weights[0]
                on_truck.insert(0, truck_weights.pop(0))
                # print(on_truck)

            else: #무게를 넘어버리면
                on_truck.insert(0,0)
                # print(on_truck)
    
    return time