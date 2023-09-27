# (0.2, lv3) Softeer_7_자동차테스트

# 자동차 연비 높 -> 연료 소비 작, 주행 거리 높

# N대 자동차
# 3대 자동차만 테스트 가능
# N대의 실제 연비 값이 주어졌을 때,
# Q개 질의에 대해 임의 3대로 골라 테스트하여 중앙값이 M_i 값이 나오는 서다 경우의 수


# === input ===
N, Q = map(int, input().split())
CAR_LIST = list(map(int, input().split()))
QUERY = [int(input()) for _ in range(Q)]

# === algorithm ===
def solution():
    car_dict = dict([(val, idx) for (idx, val) in enumerate(sorted(CAR_LIST))])

    for query in QUERY:
        if query not in car_dict:
            print(0)
        else:
            idx = car_dict[query]
            print(idx * (N - 1 - idx))


# === output ===
solution()
