# dfs__BOJ_15683_감시
# python에서 함수 인자로 전달되는 mutable object는 참조된다 -> 재귀 dfs같은 경우는 deepcopy 필요.
'''
NxM workspace
K cctv
0: EMPTY
6: WALL
1-5: CCTV (번호, 위치)
    -wall 통과 X
    -cctv 통과 O
'''

import copy

EMPTY = 0
WALL = 6
# ===input===
N, M = map(int, input().split())
WORKSPACE = [list(map(int, input().split())) for _ in range(N)]

# ===algorithm===
cctvs = list()      # (번호, 위치)
walls = list()      # 위치
for r in range(N):
    for c in range(M):
        if WORKSPACE[r][c] == WALL:
            walls.append((r, c))
        elif WORKSPACE[r][c] != EMPTY:
            cctvs.append((WORKSPACE[r][c], (r, c)))


def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < M


def check_walls(r, c):
    return (r, c) in walls


def print_space(space):
    print("=====================")
    for i in range(N):
        for j in range(M):
            print(space[i][j], end=' ')
        print()
    print("=====================")

DIRECTION_LIST = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def make_not_blind_to_direction(space, direction_id, start: tuple):
    from_r, from_c = start
    dr, dc = DIRECTION_LIST[direction_id]
    to_r, to_c = from_r + dr, from_c + dc
    while check_boundary(to_r, to_c) and not check_walls(to_r, to_c):
        space[to_r][to_c] = 7
        to_r, to_c = to_r + dr, to_c + dc
    # print_space(space)


def dfs(space, cctv_list):
    global min_blind_spot
    # space = copy.deepcopy(space)

    # 1. cctv_list 다 돌았땅
    if not cctv_list:
        blind_spot = 0
        for tr in range(N):
            for tc in range(M):
                if space[tr][tc] == EMPTY:
                    blind_spot += 1
        min_blind_spot = min(min_blind_spot, blind_spot)
        # print("\nblind_spot: ", blind_spot)
        # print_space(space)
        return

    # 2. cctv_list 아직 남았당
    curr_cctv = cctv_list[0][0]
    start_location = cctv_list[0][1]
    # print(f"\ndfs, curr_cctv: {curr_cctv} / start_location: {start_location}")
    if curr_cctv == 1:
        for direction_id in range(4):
            tmp_space = copy.deepcopy(space)
            make_not_blind_to_direction(tmp_space, direction_id, start_location)
            dfs(tmp_space, cctv_list[1:])
    elif curr_cctv == 2:
        for direction_id1, direction_id2 in [(0, 2), (1, 3)]:
            tmp_space = copy.deepcopy(space)
            make_not_blind_to_direction(tmp_space, direction_id1, start_location)
            make_not_blind_to_direction(tmp_space, direction_id2, start_location)
            dfs(tmp_space, cctv_list[1:])
    elif curr_cctv == 3:
        for direction_id1, direction_id2 in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            tmp_space = copy.deepcopy(space)
            make_not_blind_to_direction(tmp_space, direction_id1, start_location)
            make_not_blind_to_direction(tmp_space, direction_id2, start_location)
            dfs(tmp_space, cctv_list[1:])
    elif curr_cctv == 4:
        for direction_id1, direction_id2, direction_id3 in [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]:
            tmp_space = copy.deepcopy(space)
            make_not_blind_to_direction(tmp_space, direction_id1, start_location)
            make_not_blind_to_direction(tmp_space, direction_id2, start_location)
            make_not_blind_to_direction(tmp_space, direction_id3, start_location)
            dfs(tmp_space, cctv_list[1:])
    elif curr_cctv == 5:
        tmp_space = copy.deepcopy(space)
        make_not_blind_to_direction(tmp_space, 0, start_location)
        make_not_blind_to_direction(tmp_space, 1, start_location)
        make_not_blind_to_direction(tmp_space, 2, start_location)
        make_not_blind_to_direction(tmp_space, 3, start_location)
        dfs(tmp_space, cctv_list[1:])


# ===output===
min_blind_spot = N * M
# print(f"walls: {walls}, cctvs: {cctvs}")
dfs(WORKSPACE, cctvs)
print(min_blind_spot)