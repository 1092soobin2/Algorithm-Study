# DP__BOJ_2579_계단오르기
'''
1. 한 칸, 두 칸 가능
2. 세 개를 모두 밞아서는 안 된다. (시작점은 계단이 아니다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
'''
# ===input===
N = int(input())
scores = [int(input()) for _ in range(N)]

# ===algorithm===
ans = scores[0]
if N == 1:
    pass
elif N == 2:
    ans = scores[0] + scores[1]
else:
    dp = [0]*N
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(dp[0] + scores[2], 0 + scores[1] + scores[2])       # 두 칸 뛰는 경우, 한 칸 뛰는 경우
    for i in range(3, N):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
    ans = dp[N-1]

# ===output===
print(ans)