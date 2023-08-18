# (0.9, 골4) Codetree_이상한체스
# 16:10~ (50m)

# N*M
# horse [1-5: mine, 6: counter]

# cannot jump counter_horse
# each of 1-5 horses has own direction


# min ( sum( cannot go ) )

from typing import List

# === input ===
N, M = map(int, input().split())
CHESS_BOARD = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
COUNTER_HORSE = 6
DIRECTION_LIST = [[-1, 0], [0, -1], [1, 0], [0, 1]]
HORSE_DIRECTION_ID_LIST = [[],
                        [[0], [1], [2], [3]],                           # 1 horse
                        [[0, 2], [1, 3]],                               # 2 horse
                        [[0, 1], [1, 2], [2, 3], [3, 0]],               # 3 horse
                        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
                        [[0, 1, 2, 3]]]
HORSE_LOC_LIST = []
NUM_OF_HORSE = 0


def init():
    global HORSE_LOC_LIST, NUM_OF_HORSE

    for r in range(N):
        for c in range(M):
            if CHESS_BOARD[r][c] != 0 and CHESS_BOARD[r][c] != COUNTER_HORSE:
                HORSE_LOC_LIST.append([r, c])

    NUM_OF_HORSE = len(HORSE_LOC_LIST)


def sum_of_cannot_go(board: List[List[bool]]):
    ret_int = 0
    for r in range(N):
        for c in range(M):
            if not board[r][c] and CHESS_BOARD[r][c] != COUNTER_HORSE:
                ret_int += 1

    return ret_int


def go(horse_r, horse_c, direction_id_list: int, go_board: List[List[bool]]):

    def go_by_direction(direction_id):
        dr, dc = DIRECTION_LIST[direction_id]
        nr, nc = horse_r + dr, horse_c + dc     # set next location
        while 0 <= nr < N and 0 <= nc < M:
            go_board[nr][nc] = True             # check the location
            if CHESS_BOARD[nr][nc] == COUNTER_HORSE:
                break
            nr, nc = nr + dr, nc + dc           # update next location

    go_board[horse_r][horse_c] = True
    for d_id in direction_id_list:
        go_by_direction(d_id)


def get_min_sum_of_cannot_go():
    min_sum_of_cannot_go = [100]

    def dfs(go_board: List[List[bool]], horse_loc_index):
        if horse_loc_index == NUM_OF_HORSE:
            min_sum_of_cannot_go[0] = min(min_sum_of_cannot_go[0], sum_of_cannot_go(go_board))
            return

        horse_r, horse_c = HORSE_LOC_LIST[horse_loc_index]

        horse_num = CHESS_BOARD[horse_r][horse_c]

        # According to direction of horse, horse can go below locations.
        for direction_id_list in HORSE_DIRECTION_ID_LIST[horse_num]:
            new_go_board = [go_board[r][:] for r in range(N)]
            go(horse_r, horse_c, direction_id_list, new_go_board)
            dfs(new_go_board, horse_loc_index + 1)

    initial_go_board = [[False] * M for _ in range(N)]
    dfs(initial_go_board, 0)

    return min_sum_of_cannot_go[0]


def solution():
    init()
    return get_min_sum_of_cannot_go()


def print_debug(go_board, title=""):
    if not DEBUG:
        return
    print("==============================")
    print(title)
    for r in range(N):
        for c in range(M):
            char = "0" if go_board[r][c] else "_"
            print(f"{char:3}", end=" ")
        print()
    print("==============================")


# === output ===
DEBUG = False
DEBUG = True
print(solution())