def solution(storey):
    answer = 0
    
    while storey > 0:
        
        one = storey % 10
        to_floor, to_ceil = one, (10-one)
        if to_floor < to_ceil or (to_floor == 5 and (storey//10) % 10 <= 4):
            answer += to_floor
            storey = storey // 10
        else:       # to_floor > to_ceil:
            answer += to_ceil
            storey = storey // 10 + 1
        # else:       # 5층인 경우 XX45층까지만 flooring
                
        
    
    return answer
