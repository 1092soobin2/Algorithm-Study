# (0.2, 실3) DP__BOJ_1463_1로만들기

# 1. if X % 3 == 0: X //=3
# 2. if X % 2 == 0: X //=2
# 3. X -= 1

# X가 1이 아니면 1에 가까워지는 속도는 1 > 2 > 3

N = int(input())
#
def solution():

    dp = [1e9] * (N + 1)
    dp[N] = 0

    for i in range(N, 1, -1):
        if i % 3 == 0 and i % 2 == 0:
            dp [i]
        if i % 3 == 0:
            dp[i // 3] = min(dp[i // 3], dp[i] + 1)
        if i % 2 == 0:
            dp[i // 2] = min(dp[i // 2], dp[i] + 1)
        dp[i - 1] = min(dp[i - 1], dp[i] + 1)

    return dp[1]


# def solution():
#
#     dp = [None] * (N + 1)
#
#     dp[1] = 0
#
#     def recursive(n):
#         if dp[n]:
#             return dp[n]
#
#         if n % 3 == 0 and n % 2 == 0:
#             dp[n] = min(recursive(n % 3) + 1, recursive(n % 2) + 1)
#         elif n % 3 == 0:
#             dp[n] = min(recursive(n % 3) + 1, recursive(n - 1) + 1)
#         elif n % 2 == 0:
#             dp[n] = min(recursive(n % 2) + 1, recursive(n - 1) + 1)
#         else:
#             dp[n] = recursive(n - 1) + 1
#
#         return dp[n]
#
#     return recursive(N)

print(solution())
