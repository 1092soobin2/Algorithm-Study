def solution(alp: int, cop: int, problems):
    answer = 0      # 모든 문제를 풀 수 있는 (알, 코)를 얻는 시간

    MAX_P = 151
    
    # 달성해야 하는 알고력, 코딩력 찾기
    max_alp, max_cop = 0, 0
    for a_req, c_req, _, _, _ in problems:
        max_alp = max(max_alp, a_req)
        max_cop = max(max_cop, c_req)
    
    
    # if alp >= max_alp and cop >= max_cop:
    #     return 0
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    def print_arr(arr):
        for r in range(alp, max_alp+1):
            for c in range(cop, max_cop + 1):
                print(arr[r][c] if arr[r][c] != 1e9 else "_", end='')
            print()
            
    # dp
    dp = [[1e9]*(MAX_P+1) for _ in range(MAX_P+1)]
    dp[alp][cop] = 0
    for r in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            # 시간 1 흐르는 경우
            if r+1 <= max_alp:
                dp[r+1][c] = min(dp[r+1][c], dp[r][c] + 1)
            if c+1 <= max_cop:
                dp[r][c+1] = min(dp[r][c+1], dp[r][c] + 1)
            # 문제를 푸는 경우
            for a_req, c_req, a_rwd, c_rwd, cost in problems:
                if r >= a_req and c >= c_req:
                    nr, nc = min(r+a_rwd, max_alp), min(c+c_rwd, max_cop)
                    dp[nr][nc] = min(dp[nr][nc], dp[r][c] + min(cost, abs(nr-r)+ abs(nc-c)))
    
    answer = dp[max_alp][max_cop]
        
    return answer
