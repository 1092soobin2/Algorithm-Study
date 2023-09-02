# (1, 골5) DP__BOJ_15486_퇴사2

# 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없
# N+1일 째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없

# answer: 얻을 수 있는 최대 수익

import sys

# === input ===
N = int(input())
# T_P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# === algorithm ===
def solution():

    # 최대 가격을 저장하는 리스트
    dp = [0] * (N + 2)

    for i in range(1, N + 1):
        # time, price = T_P[i-1]
        time,price = map(int, sys.stdin.readline().split())
        # dp[i] = max(dp[i], dp[i - 1])

        if dp[i] < dp[i - 1]:
            dp[i] = dp[i - 1]

        if i + time <= N + 1:
            if dp[i + time] < (dp[i] + price):
                dp[i + time] = dp[i] + price
        #     dp[i + time] = max(dp[i + time], dp[i] + price)

        # print(i, dp)

    # 뒤에서 50개 검사.
    return max(dp[-2:])


# === output ===
print(solution())

