N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(i + 1) for i in range(N)]

dp[0][0] = triangle[0][0]
for i in range(len(triangle) - 1):
    for j in range(i + 1):
        dp[i + 1][j] = max(dp[i + 1][j], triangle[i + 1][j] + dp[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], triangle[i + 1][j + 1] + dp[i][j])

print(max(dp[N - 1]))
