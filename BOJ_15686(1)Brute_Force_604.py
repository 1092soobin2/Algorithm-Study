# BOJ_15686 Graph Algorithm

### input
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

### algorithm
from itertools import combinations

# 1. 집, 치킨
HOUSE, CHICKEN = 1, 2
houses, chickens = list(), list()

for i in range(N):
    for j in range(N):
        if city[i][j] == HOUSE: houses.append((i,j))
        elif city[i][j] == CHICKEN: chickens.append((i,j))

# 2. 가능한 모든 치킨 집의 조합
min_sum_of_dist = 1e9
for chickens1 in combinations(chickens, M):
    sum_of_dist = 0
    # 각 집별 최소 치킨 거리
    for house in houses:
        min_dist = 1e9
        for chicken in chickens1:
            min_dist = min(min_dist, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        sum_of_dist += min_dist
    min_sum_of_dist = min(min_sum_of_dist, sum_of_dist)

### output
print(min_sum_of_dist)