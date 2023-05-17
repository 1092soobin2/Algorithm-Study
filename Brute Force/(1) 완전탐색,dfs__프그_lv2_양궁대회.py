def solution(n, info):
    answer = [0]*11
    max_diff = [0]
    
    # now: 현재 위치
    # acc: 교무
    def dfs(now, acc, apeach, ryan):
        
        # 화살 초과
        if sum(acc) > n:
            return
        
        # 화살 다 씀
        if sum(acc) == n:
            # 0. 점수 정산
            for i in range(now, 11):
                if info[i] != 0:
                    apeach += (10 - i)
            # 1. 가장 큰 점수 차이 (ryan - apeach > 0 이어야 함))
            if max_diff[0] < (ryan - apeach):
                max_diff[0] = (ryan - apeach)
                answer[:] = acc
            # 2. 낮은 점수 많이 맞힌 acc
            elif max_diff[0] == (ryan - apeach):
                for i in range(10, -1, -1):
                    if acc[i] == answer[i]:
                        continue
                    else:
                        if acc[i] > answer[i]:
                            answer[:] = acc
                        break
            return
        
        # 마지막 0점인 경우
        if now == 10:
            acc[now] = n - sum(acc)
            dfs(now + 1, acc, apeach, ryan)
            acc[now] = 0
            return
                
        # lion이 점수 가지는 경우
        acc[now] = info[now] + 1
        dfs(now + 1, acc, apeach, ryan + (10 - now))
        acc[now] = 0


        # lion이 점수 안 가지는 경우 (apeach가 가지는 경우/ 아닌 경우)
        if info[now] == 0:
            dfs(now + 1, acc, apeach, ryan)
        else:
            dfs(now + 1, acc, apeach + (10 - now), ryan)
        
        
    dfs(0, [0]*11, 0, 0)
    
    if max_diff[0] == 0:
        answer = [-1]
    return answer
