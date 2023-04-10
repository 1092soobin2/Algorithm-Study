def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0]*bridge_length
    sum_of_weights = 0
    
    while truck_weights:
        
        # 1초가 경과한다.
        truck = bridge.pop(0)
        sum_of_weights -= truck
        answer += 1
        
        # 트럭을 태운다.
        if sum_of_weights + truck_weights[0] <= weight:
            new_truck = truck_weights.pop(0)
            bridge.append(new_truck)
            sum_of_weights += new_truck
        else:
            bridge.append(0)
        
        # print(f"{answer}sec, weightsum:{sum_of_weights} {bridge}")
        
    
    answer += bridge_length
    
    return answer
