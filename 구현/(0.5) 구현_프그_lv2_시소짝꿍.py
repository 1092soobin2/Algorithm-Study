def solution(weights):
    answer = 0
    
    # (무게) * (축-좌석)
    weight_list = [0]*1001
    for weight in weights:
        answer += weight_list[weight]
        weight_set = set()
        for dist1 in [2, 3, 4]:
            for dist2 in [2, 3, 4]:
                if (dist1 * weight) % dist2 == 0:
                    weight_set.add((dist1 * weight) // dist2)
        for w in list(weight_set):
            if 100 <= w <= 1000:
                weight_list[w] += 1
            
    return answer
