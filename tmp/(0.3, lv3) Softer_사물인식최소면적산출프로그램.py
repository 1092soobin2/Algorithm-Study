import sys

# (0.3, lv3) Softer_사물인식최소면적산출프로그램

# N point
# K color

# 한 위치에 여러 개의 점 존재 가능

# =========
N, K = map(int, input().split())
POINT_LIST = [list() for _ in range(K)]


# =========
def init():
    global POINT_LIST
    for _ in range(N):
        x, y, k = map(int, input().split())
        POINT_LIST[k - 1].append([x, y])
    # print_debug(f"init() done. POINT_LIST: {POINT_LIST}")


answer = int(1e7)


def solution():

    def get_width(min_r, min_c, max_r, max_c):
        return (max_r - min_r) * (max_c - min_c)

    def dfs(color_idx, min_r, min_c, max_r, max_c):
        global answer
        if color_idx == K:
            answer = min(answer, get_width(min_r, min_c, max_r, max_c))
            return

        if get_width(min_r, min_c, max_r, max_c) >= answer:
            return

        for r, c in POINT_LIST[color_idx]:
            dfs(color_idx + 1, min(min_r, r), min(min_c, c), max(max_r, r), max(max_c, c))

    init()
    for tr, tc in POINT_LIST[0]:
        dfs(1, tr, tc, tr, tc)

    return answer


def print_debug(title=""):
    if not DEBUG:
        return

    print("==================================")
    print(title)
    print("==================================")


# =========
DEBUG = False
DEBUG = True
print(solution())
