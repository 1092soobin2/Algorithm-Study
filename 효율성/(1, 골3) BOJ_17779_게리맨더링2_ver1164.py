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
TOTAL_POPULARITY = sum(sum(POPULARITY))


# === algorithm ===
def get_sum_of_popularity(region: List[List[int]]):
    sum_list = [0] * 5

    for r in range(N):
        for c in range(N):
            sum_list[region[r][c] - 1] += POPULARITY[r][c]
        max_now = max(sum_list)

    return sum_list


def mark_region(x, y, d1, d2):
    region = [[0]*N for _ in range(N)]

    for edge1 in range(d1 + 1):
        region[x + edge1][y - edge1] = 5
        region[x + d2 + edge1][y + d2 - edge1] = 5
    for edge2 in range(d2 + 1):
        region[x + edge2][y + edge2] = 5
        region[x + d1 + edge2][y - d1 + edge2] = 5

    flag_5 = False
    for r in range(N):
        for c in range(N):
            if region[r][c] == 5:
                if r == x or r == (x + d1 + d2):        # 현재 row에 5 선거구 1 구역밖에 없는 경우
                    continue
                else:                                   # 현재 row에 5 선거구 1 구역 초과인 경우
                    if flag_5:                          # 5 선거구 오른쪽 경계
                        flag_5 = False
                    else:                               # 5 선거구 왼쪽 경계
                        flag_5 = True
            elif flag_5:                                # 5 선거구 내부
                region[r][c] = 5
            else:                                       # 1, 2, 3, 4 구역
                if r < x + d1 and c <= y:
                    region[r][c] = 1
                elif r <= x + d2 and c > y:
                    region[r][c] = 2
                elif r >= x + d1 and c < y - d1 + d2:
                    region[r][c] = 3
                elif r > x + d2 and c >= y - d1 + d2:
                    region[r][c] = 4

    print_debug(region, title=f"after mark_region()")

    return region


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

    for [x, y, d1, d2] in divide_region():
        region = mark_region(x, y, d1, d2)
        sum_list = get_sum_of_popularity(region)
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
