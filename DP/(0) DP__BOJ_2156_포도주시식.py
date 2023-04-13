# (0) DP__BOJ_2156_포도주시식
'''
1. 선택한 잔 마시깅
2. 연속 3잔 불가능

ans: 최대한 많은 양의 포도주
'''
# ===input===
n = int(input())
wines = [int(input()) for _ in range(n)]

# ===algorithm===
ans = wines[0]
dp = [0]*n
dp2 = [0]*n
if n == 1:
    pass
elif n == 2:
    ans += wines[1]
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(dp[0] + wines[2], 0 + wines[1] + wines[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i], dp[i-1])
    ans = dp[n-1]


# ===output===
print(ans)