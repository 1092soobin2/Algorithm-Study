# (1.3, 골1) BOJ_19236_청소년 상어


# 4*4 Grid
# 1칸에 1 Fish
# Fish [Id(1-16), Direction(1-8)]

# Shark [Location, Direction]
# 물고기를 먹음
# (0,0)에 들어가서, (0,0) 물고기부터 먹음

# Fish: Move


# Shark: move
# 물고기 이동이 끝나면 상어가 이동
# 이동 가능한 칸 X -> 집으로 간다.
# Fish O 칸으로 이동하여, 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
# 이동 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
# Fish X 칸으로는 이동 X

# ans: 상어가 먹을 수 있는 물고기 번호 합의 최댓값.

from typing import List
import copy

DIRECTION_LIST = [[-1, 1], [-1, 0], [-1, -1], [0, -1],
                  [1, -1], [1, 0], [1, 1], [0, 1]]
LEN_GRID = 4


# === input ===
fish_board_0 = [[0]*LEN_GRID for _ in range(LEN_GRID)]        # only FISH NUMBER
fish_dict_0 = dict()                                          # [ALIVE, FISH_DIR, FISH_LOC]
ALIVE, FISH_DIR, FISH_LOC = 0, 1, 2                         # for fish access
# shark = [[0, 0], 0]
SHARK_LOC, SHARK_DIR = 0, 1                                 # for shark access


# === algorithm ===
def init():
    global fish_board_0, fish_dict_0

    for r in range(LEN_GRID):
        input_line = list(map(int, input().split()))
        for c in range(LEN_GRID):
            fish_dict_0[input_line[2 * c]] = [True, input_line[2 * c + 1] % 8, [r, c]]
            fish_board_0[r][c] = input_line[2 * c]

    print_debug(fish_dict_0, fish_board_0, "init() done.")


def move_fishes(fish_dict, shark, fish_board):

    # 번호 작은 순으로 이동. -> TODO: dict
    # 한 칸 이동 가능
    for fish_num in range(1, 17):
        if not fish_dict[fish_num][ALIVE]:
            continue

        r, c = fish_dict[fish_num][FISH_LOC]
        d = fish_dict[fish_num][FISH_DIR]

        while True:
            dr, dc = DIRECTION_LIST[d]
            nr, nc = r + dr, c + dc

            # 이동 X: 상어 칸 || 경계 밖
            if [nr, nc] == shark[SHARK_LOC] or not (0 <= nr < LEN_GRID and 0 <= nc < LEN_GRID):
                d = (d + 1) % 8                             # 이동 가능한 칸을 향할 때까지 반시계 회전
                if d == fish_dict[fish_num][FISH_DIR]:      # 이동 가능한 칸이 없으면 이동 X
                    break
            # 이동 O: 빈 칸 || 다른 물고기가 있는 칸
            else:
                fish_dict[fish_num][FISH_DIR] = d
                another_fish_num = fish_board[nr][nc]
                # 다른 물고기가 있는 칸은 서로의 위치를 바꾼다.
                fish_board[nr][nc], fish_board[r][c] = fish_board[r][c], fish_board[nr][nc]
                fish_dict[fish_num][FISH_LOC], fish_dict[another_fish_num][FISH_LOC] = [nr, nc], [r, c]
                break
        print_debug(fish_dict, fish_board, shark, f"after move shark {fish_num}" )


def recursive(shark, acc, fish_board, fish_dict):
    global answer

    def get_next_loc_list():
        ret_list = []

        [nr, nc], d = shark
        dr, dc = DIRECTION_LIST[d]

        nr, nc = nr + dr, nc + dc
        while 0 <= nr < LEN_GRID and 0 <= nc < LEN_GRID:
            if fish_dict[fish_board[nr][nc]][ALIVE]:
                ret_list.append([nr, nc])
            nr, nc = nr + dr, nc + dc
        return ret_list

    # eat fish
    r, c = shark[SHARK_LOC]
    acc += fish_board[r][c]
    shark[SHARK_DIR] = fish_dict[fish_board[r][c]][FISH_DIR]
    fish_dict[fish_board[r][c]][ALIVE] = False

    print_debug(fish_dict, fish_board, shark, f"in recursive, after eating fish, acc: {acc} ")
    # move fishes
    move_fishes(fish_dict, shark, fish_board)
    # move shark
    next_loc_list = get_next_loc_list()
    if next_loc_list:
        for next_loc in next_loc_list:
            recursive([next_loc, shark[SHARK_DIR]], acc, copy.deepcopy(fish_board), copy.deepcopy(fish_dict))
    else:
        answer = max(acc, answer)
        return


def print_debug(fish_dict, fish_board, shark=None, title=""):
    if not DEBUG:
        return

    print("=======================================")
    print(title, shark)
    for r in range(LEN_GRID):
        for c in range(LEN_GRID):
            fish_num = fish_board[r][c]
            if fish_dict[fish_num][ALIVE]:
                print(f"[num: {fish_num}, dir: {fish_dict[fish_num][FISH_DIR]}]", end="\t")
            else:
                print(f"\t\t\t\t\t", end="")
        print()
    print("=======================================")


# === output ===
DEBUG = False
init()
answer = 0
recursive([[0, 0], 0], 0, fish_board_0, fish_dict_0)
print(answer)
