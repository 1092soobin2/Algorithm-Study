def solution(m, n, puddles):
    # [1, 1] ~ [n, m]
    
    dp = [[1]*m for _ in range(n)]
    
    for c, r in puddles:
        dp[r - 1][c - 1] = 0
    
    # case: r = 0
    for c in range(1, m):
        if dp[0][c] == 0:
            continue
        else:
            dp[0][c] = dp[0][c - 1]
    
    # case: c = 0
    for r in range(1, n):
        if dp[r][0] == 0:
            continue
        else:
            dp[r][0] = dp[r - 1][0]
        
    for r in range(1, n):
        for c in range(1, m):
            if dp[r][c] == 0:
                continue
            else:
                dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % (1e9 + 7)
                
    return dp[n - 1][m - 1] % (1e9 + 7)
