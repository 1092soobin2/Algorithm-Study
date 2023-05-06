# (1.5, 플5) __BOJ_23291_어항정리




# 어항 정리
# 1. min(물고기수) 어항들에 -> +1
# 2. 공중 부양
#     1) 어항0을 어항1 위에 쌓는다.
#     2) 2개 이상 쌓인 어항을 시계방향으로 90도 회전시켜 샇는다.
#     3) 2)를 공중부양하는 어항이 없을 때까지 반복

# 3. 물고기 수 조절
#     1) (차이) // 5 == d
#     2) d > 0 -> 적은 곳에 d마리를 이동시킨다.
#     3) 모든 인접 칸에 대해 동시 발생
# TODO: list에 담고 나중에 처리해주기

# 4. 바닥에 놓기

# 5. 공중 부양 N/2 -> N/4
# 6. 조절
# 7. 바닥에 놓기

# max - min <= K 이하가 되도록 하는 어항 정리 횟수

# ===input===
N, K = map(int, input().split())
fishbowl = list(map(int, input().split()))


# ===algorithm===
def add_fish():
    global fishbowl
    min_fish = min(fishbowl)
    for i in range(N):
        if fishbowl[i] == min_fish:
            fishbowl[i] += 1


def stack_fishbowl_1():
    global fishbowl

    def rotate_clockwise(arr, len_r, len_c):

        ret_new_arr = []
        rotated = [[0]*len_r for _ in range(len_c)]

        # rotated 부분 구하기
        for r in range(len_r):
            for c in range(len_c):
                rotated[len_c - 1 - c][r] = arr[r][c]

        # rotated 부분 쌓기
        ret_new_arr = [arr[0][len_c:]]
        for _ in range(len_c):
            ret_new_arr += [[None] * len(ret_new_arr[0])]
        for r in range(len_c):
            for c in range(len_r):
                ret_new_arr[1 + r][c] = rotated[r][c]

        return ret_new_arr, len_c + 1, len_r

    len_row, len_col = 2, 1
    stacked_fishbowl = [fishbowl[1:], [fishbowl[0]]]

    while (len(stacked_fishbowl[0]) - len_col) >= len_row:
        stacked_fishbowl, len_row, len_col = rotate_clockwise(stacked_fishbowl, len_row, len_col)

    return stacked_fishbowl


def adjust_fishbowl(arr):

    len_row = len(arr)
    len_col = len(arr[0])

    adjusted = [[0]*len_col for _ in range(len_row)]

    for r in range(len_row):
        for c in range(len_col):
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                if not arr[r][c]:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < len_row and 0 <= nc < len_col and arr[nr][nc]:
                    diff = (abs(arr[r][c] - arr[nr][nc])) // 5
                    if diff > 0:
                        if arr[r][c] > arr[nr][nc]:
                            adjusted[nr][nc] += diff
                        else:
                            adjusted[nr][nc] -= diff

    for r in range(len_row):
        for c in range(len_col):
            if arr[r][c]:
                arr[r][c] += adjusted[r][c]

    return fishbowl


def spread_fishbowl(arr):

    new_arr = [0]*N

    i_new_arr = 0
    len_row, len_col = len(arr), len(arr[0])

    # stacked
    for c in range(len_col):
        for r in range(len_row):
            if arr[r][c]:
                new_arr[i_new_arr] = arr[r][c]
                i_new_arr += 1

    return new_arr


def stack_fishbowl_2():
    ret_fishbowl = [0]*4

    division = N // 4

    # 0
    ret_fishbowl[0] = fishbowl[3 * division:]
    # 1
    ret_fishbowl[1] = fishbowl[:division][::-1]
    # 2
    ret_fishbowl[2] = fishbowl[division:2*division]
    # 3
    ret_fishbowl[3] = fishbowl[2*division:3*division][::-1]

    return ret_fishbowl


def check_diff() -> bool:
    return (max(fishbowl) - min(fishbowl)) <= K

# ===output===
answer = 0
while not check_diff():
    add_fish()
    fishbowl = stack_fishbowl_1()
    fishbowl = adjust_fishbowl(fishbowl)
    fishbowl = spread_fishbowl(fishbowl)
    fishbowl = stack_fishbowl_2()
    fishbowl = adjust_fishbowl(fishbowl)
    fishbowl = spread_fishbowl(fishbowl)
    answer += 1

print(answer)
