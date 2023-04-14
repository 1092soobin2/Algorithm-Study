def solution(stones, k):
    answer = 1e9

    # (stones[i]) > 0 이어야 밟을 수 있다.
    # (stones[i]) == 0 이면 0 이상인 최단 디딤돌로 건넌다. 여러 칸 건넌다.
    # 밟을 때마다 - 1
    # k: 최대 점프 간격
    # 최대 몇명까지 건널 수 있는지
    
    niniz_min, niniz_max = 1, 200000000
    
    while niniz_min < niniz_max:
        mid = (niniz_min + niniz_max) // 2
        
        # 연속 k개 불능 -> O(N)
        k_flag = False
        cnt = 0
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt >= k:
                    k_flag = True
            else:
                cnt = 0      
                
        if k_flag:
            niniz_max = mid
        else:
            niniz_min = mid+1
    
    answer = niniz_max

    return answer
