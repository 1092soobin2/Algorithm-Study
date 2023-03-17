# BOJ_15686(2)Brute_Force
# ===input===
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# ===algorithm===
from itertools import combinations

# 1. 집, 치킨
HOUSE, CHICKEN = 1, 2
houses, chickens = [], []

for i in range(N):
    for j in range(N):
        if city[i][j] == HOUSE: houses.append((i,j))
        elif city[i][j] == CHICKEN: chickens.append((i,j))

# 2. 치킨 거리
def cal_dist(chicken_list):
    sum_of_dist = 0
    for [h0, h1] in houses:
        min_dist = 1e9
        for [c0, c1] in chicken_list:
            min_dist = min(min_dist, abs(h0 - c0) + abs(h1 - c1))
        sum_of_dist += min_dist
    return sum_of_dist



# 3. 가능한 모든 치킨 집의 조합

min_sum_of_dist = 1e9
for chickens1 in combinations(chickens, M):
    min_sum_of_dist = min(min_sum_of_dist, cal_dist(chickens1))

# ===output===
print(min_sum_of_dist)
