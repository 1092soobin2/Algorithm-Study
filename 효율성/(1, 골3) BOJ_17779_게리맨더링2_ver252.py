# (1, 골3) BOJ_17779_게리맨더링2

# N*N grid

# 5 region
# 구역을 적어도 1 포함
# 모두 연결되어 있어ㅑ
# A -> B 로 이동할 수 있을 때, 두 구역은 연결되어 있다고 한다.
# 중간에 통하는 인접 구역은 0개 이상
# 모두 같은 region 에 포함되어야

# 기준점 X, Y
# 경계의 길이 D1, D2


# 1 2
#  5
# 3 4

# 선거구의 인구 = sum(popularity)
# min (max(pop) min(pop))

from typing import List


# === input ===
N = int(input())
POPULARITY = [list(map(int, input().split())) for _ in range(N)]
TOTAL_POPULARITY = 0
ACC_POPULARITY = []


# === algorithm ===
def init():
    global ACC_POPULARITY, TOTAL_POPULARITY

    ACC_POPULARITY = [[0]*(N + 1) for _ in range(N + 1)]

    for r in range(N):
        ACC_POPULARITY[r][0] = POPULARITY[r][0]
        for c in range(1, N):
            ACC_POPULARITY[r][c] = ACC_POPULARITY[r][c - 1] + POPULARITY[r][c]
        TOTAL_POPULARITY += ACC_POPULARITY[r][N - 1]


def get_sum_of_popularity(x, y, d1, d2):
    sum_list = [0] * 6

    [x2, y2], [x3, y3], [x4, y4] = [x + d2, y + d2], [x + d1, y - d1], [x + d1 + d2, y - d1 + d2]

    # district 1
    for r in range(x):
        sum_list[1] += ACC_POPULARITY[r][y]
    for edge1 in range(d1):
        sum_list[1] += ACC_POPULARITY[x + edge1][y - edge1 - 1]

    # 2
    for r in range(x):
        sum_list[2] += ACC_POPULARITY[r][N - 1] - ACC_POPULARITY[r][y]
    for edge2 in range(d2 + 1):
        sum_list[2] += ACC_POPULARITY[x + edge2][N - 1] - ACC_POPULARITY[x + edge2][y + edge2]

    # 3
    for r in range(x4 + 1, N):
        sum_list[3] += ACC_POPULARITY[r][y4 - 1]
    for edge2 in range(d2 + 1):
        sum_list[3] += ACC_POPULARITY[x3 + edge2][y3 + edge2 - 1]

    # 4
    for r in range(x4 + 1, N):
        sum_list[4] += ACC_POPULARITY[r][N - 1] - ACC_POPULARITY[r][y4 - 1]
    for edge1 in range(1, d1 + 1):
        sum_list[4] += ACC_POPULARITY[x2 + edge1][N - 1] - ACC_POPULARITY[x2 + edge1][y2 - edge1]

    sum_list[5] = TOTAL_POPULARITY - sum(sum_list[:5])

    return sum_list[1:]


def divide_region() -> List[int]:
    possible_district = []

    for r in range(N - 2):
        for c in range(1, N - 1):
            district = [r, c]
            for d1 in range(1, min(c, (N - 1) - r - 1) + 1):
                for d2 in range(1, min(N - (r + d1) - 1, (N - 1) - c) + 1):
                    possible_district.append(district + [d1, d2])

    print_debug(POPULARITY, title=f"divide_region\nresult:{possible_district}")
    return possible_district


def solution():
    answer = 1e9

    init()
    for [x, y, d1, d2] in divide_region():
        sum_list = get_sum_of_popularity(x, y, d1, d2)
        answer = min(answer, max(sum_list) - min(sum_list))

    return answer


def print_debug(arr, title=""):
    if not DEBUG:
        return

    print("====================================")
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{arr[r][c]:4}", end="")
        print()
    print("====================================")


# === output ===
DEBUG = False
# DEBUG = True
print(solution())
