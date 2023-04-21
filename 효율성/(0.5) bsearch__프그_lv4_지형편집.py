from collections import defaultdict

def solution(land, P, Q):
    answer = -1
    
    
    land_dict = defaultdict(int)
    N = len(land)
    for r in range(N):
        for c in range(N):
            land_dict[land[r][c]] += 1
    
    
    def calculate_cost(level) -> int:
        # P: adding cost, Q: removing cost
        ret_cost = 0
        for lv, num in land_dict.items():
            if lv > level:
                ret_cost += (lv-level) * num * Q
            elif lv < level:
                ret_cost += (level-lv) * num * P
        return ret_cost
            
        
    min_lv, max_lv = 0, 1e9
    while min_lv <= max_lv:
        mid = (min_lv + max_lv) // 2
        cost = [calculate_cost(mid - 1), calculate_cost(mid), calculate_cost(mid + 1)]
        # print(mid, cost)
        if min(cost) == cost[1]:
            answer = cost[1]
            break
        elif min(cost) == cost[0]:
            max_lv = mid
        elif min(cost) == cost[2]:
            min_lv = mid + 1
        
    return answer
