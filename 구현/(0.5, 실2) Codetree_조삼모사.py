# (0.5, 실2) Codetree_조삼모사

# N works
# N is multiple of 2.
# [4, 20]

# P work intensity 2d-array
# P[i][i] = 0
# P[i][j]     [1, 100]


from typing import List
from itertools import combinations

# === input ===
N: int = int(input())
P: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
# nCr
def combination(arr: List[int], n, r, two=False):
    ret_list = []

    def dfs(start_idx, accumulated_int, accumulated_list):
        if not two:
            if accumulated_int == r:
                ret_list.append(accumulated_list[:])
                return
        else:
            if accumulated_int == (r - 1):
                ret_list.append([arr[0]] + accumulated_list[:])
                return

        for idx in range(start_idx, n):
            dfs(idx + 1, accumulated_int + 1, accumulated_list + [arr[idx]])

    if not two:
        dfs(0, 0, [])
    else:
        dfs(1, 0, [])

    return ret_list


def get_intensity(work_list):
    intensity = 0
    # for [i, j] in combination(work_list, N // 2, 2):
    #     intensity += P[i][j] + P[j][i]

    for i in range(N//2):
        for j in range(i + 1, N//2):
            intensity = intensity + (P[work_list[i]][work_list[j]] + P[work_list[j]][work_list[i]])

    return intensity


def solution():

    ans = 1e9       # min ( morning_intensity - evening_intensity )

    work_list = list(range(N))
    # morning_work_list = combination(work_list, N, N // 2)
    # morning_work_list = list(combinations(work_list, N // 2))         # 별 차이 없음. 928(내꺼), 955(모듈)
    # morning_work_list = morning_work_list[:len(morning_work_list)//2]

    morning_work_list = combination(work_list, N, N // 2, two=True)

    for morning_work in morning_work_list:
        # evening_work = list(filter(lambda x: x not in morning_work, work_list))

        ans = min(ans, abs(get_intensity(morning_work) - get_intensity(evening_work)))

    return ans


# === output ===
print(solution())
