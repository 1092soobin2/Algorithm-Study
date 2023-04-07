# (0.5) DP__BOJ_14501_퇴사


# ===input===
N = int(input())
end_day_list = [list() for _ in range(N+1)]      # day_list[end_day] = [(day1, price), (day2
for day in range(1, N+1):
    time, price = map(int, input().split())
    end_day = day+time-1
    if end_day <= N:
        end_day_list[end_day].append((day, price))


# ===algorithm===
dp = [0]*(N+1)
for end_day, day_price_list in enumerate(end_day_list):
    dp[end_day] = dp[end_day-1]
    for day, price in day_price_list:
        dp[end_day] = max(dp[end_day], dp[day-1] + price)


# ===output===
print(dp[N])