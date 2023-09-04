# (0.2, 실2) DP__BOJ_2748_피보나치수


N = int(input())


# 44ms
def bottom_up_tabulation():
    dp = [None] * (N + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]


# 44ms
def top_down_memoization():
    dp = [None] * (N + 1)

    def fibonacci(n):

        if n == 0:
            return 0
        if n == 1:
            return 1

        if dp[n]:
            return dp[n]

        dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return dp[n]

    return fibonacci(N)


# 시간 초과
def top_down():

    def fibonacci(n):

        if n == 0:
            return 0
        if n == 1:
            return 1

        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci(N)


# 48ms
def bottom_up_only2():
    x, y = 0, 1
    for i in range(2, N + 1):
        x, y = y, x + y

    return y


# print(bottom_up_memoization())
# print(top_down_memoization())
# print(top_down())
print(bottom_up_only2())
