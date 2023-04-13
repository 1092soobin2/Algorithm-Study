# (3) 구현,dfs__BOJ_23290_마법사상어와복제 1h
# 시간 초과: remove: O(N)

import copy

EDGE = 4
fish_direction_list = [(1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1),
                  (0, 1), (1, 1), (1, 0), (1, -1)]

scent_board = [[0]*EDGE for _ in range(EDGE)]
fish_board = [[0]*EDGE for _ in range(EDGE)]
fishes = [[[0]*8 for _ in range(EDGE)] for _ in range(EDGE)]


# ===input===
M, S = map(int, input().split())
for _ in range(M):
    fish_r, fish_c, fish_d = map(int, input().split())
    fish_r, fish_c = fish_r-1, fish_c-1
    fish_board[fish_r][fish_c] += 1
    fishes[fish_r][fish_c][fish_d%8] += 1
shark_r, shark_c = map(lambda x: x - 1, map(int, input().split()))


# ===algorithm===
# 마법 연습
# 1. 모든 물고기에게 복제 마법 시전
def duplicate_fishes():
    global fishes
    dup_fishes = copy.deepcopy(fishes)
    return dup_fishes


# 2. 모든 물고기가 한 칸 이동한다.
def move_fishes():
    global fishes
    copied_fishes = copy.deepcopy(fishes)
    for curr_r in range(EDGE):
        for curr_c in range(EDGE):
            # for curr_d in copied_fishes[curr_r][curr_c]:
            for curr_d in range(8):
                if copied_fishes[curr_r][curr_c][curr_d] != 0:
                    # 1) 이동 X: 상어 있는 칸, 물고기의 냄새가 있는 칸, 격자 밖
                    # 2) 이동 가능한 칸을 향할 때까지 45도 반시계 회전
                    for counter_clockwise in range(8):
                        next_d = (curr_d - counter_clockwise) % 8
                        dr, dc = fish_direction_list[next_d]
                        nr, nc = curr_r+dr, curr_c+dc
                        if 0 <= nr < EDGE and 0 <= nc < EDGE:
                            if not (nr == shark_r and nc == shark_c) and scent_board[nr][nc] == 0:
                                # fishes[curr_r][curr_c].remove(curr_d)
                                # fishes[nr][nc].append(next_d)
                                n = copied_fishes[curr_r][curr_c][curr_d]
                                fishes[nr][nc][next_d] += n
                                fishes[curr_r][curr_c][curr_d] -= n
                                fish_board[curr_r][curr_c] -= n
                                fish_board[nr][nc] += n
                                break
            # 3) 이동할 수 있는 칸이 X -> 이동 X


# 3. 상어가 연속 3칸 이동
def move_shark():
    global shark_r, shark_c

    shark_direction_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # 1) 상하좌우로 이동 가능
    # 2) 물고기가 가장 많이 제거되도록 이동
    # 3) 여러 가지라면 사전순
    orders = []         # (num_of_fishes, direction_ids) e.g.(3, [1, 2, 3])
    # max_num_of_fishes = 0

    # fish_board W(by copy), scent_board RO
    def dfs(arr, now_r, now_c, acc_order: list, acc_num: int):
        if len(acc_order) == 3:
            # TODO: 왜 여기서 orders (list)는 접근 가능하고 max_num.. (int)는 접근 불가한 거지?
            orders.append((acc_num, acc_order))
            return

        # TODO: deepcopy 개수 줄이고 시간 차이 확인
        for d_id, (dr, dc) in enumerate(shark_direction_list):
            nr, nc = now_r+dr, now_c+dc
            if 0 <= nr < EDGE and 0 <= nc < EDGE:
                arr = copy.deepcopy(arr)
                num = arr[nr][nc]
                arr[nr][nc] = 0
                dfs(arr, nr, nc, acc_order + [d_id], acc_num+num)

    dfs(fish_board, shark_r, shark_c, [], 0)
    orders.sort(key=lambda x: (-x[0], x[1][0], x[1][1], x[1][2]))
    order = orders[0][1]

    # 4) 연속해서 이동하는 중에 물고기가 있는 칸 -> 물고기들이 제외되고 냄새를 남긴다.

    for direction_id in order:
        dr, dc = shark_direction_list[direction_id]
        shark_r, shark_c = shark_r+dr, shark_c+dc
        # 격자 안 벗어나도록 order를 구함.
        if fish_board[shark_r][shark_c] != 0:
            fishes[shark_r][shark_c] = [0]*8
            fish_board[shark_r][shark_c] = 0
            scent_board[shark_r][shark_c] = 2


# 4. 물고기의 냄새는 2번 이후 사라진다.
def update_scent_board():
    for r in range(EDGE):
        for c in range(EDGE):
            if scent_board[r][c] > 0:
                scent_board[r][c] -= 1


# 5. 1번에서 복제된 물고기가 생긴다. 1에서의 위치, 방향을 가진다.
def create_duplicated(dup_fishes):
    global fishes
    for r in range(EDGE):
        for c in range(EDGE):
            # fishes[r][c] += dup_fishes[r][c]
            # fish_board[r][c] += len(dup_fishes[r][c])
            for d in range(8):
                fishes[r][c][d] += dup_fishes[r][c][d]
            fish_board[r][c] += sum(dup_fishes[r][c])

# ans
def sum_of_fishes():
    return sum(list(map(sum, fish_board)))


def print_fish_board(arr, arr2=()):
    print("==============")
    for r in range(EDGE):
        for c in range(EDGE):
            print(arr[r][c], end=' ')
        print("\t\t", end='')
        if len(arr2) != 0:
            for c in range(EDGE):
                print(arr2[r][c], end=' ')
        print()
    print("==============")


# ===output===
dup = duplicate_fishes()
move_fishes()
move_shark()
create_duplicated(dup)

for _ in range(S-1):
    dup = duplicate_fishes()

    move_fishes()
    # print("move fishes")
    # print_fish_board(fish_board)

    update_scent_board()
    move_shark()
    # print("move sharks", shark_r, shark_c)
    # print_fish_board(fish_board)

    create_duplicated(dup)
    # print("fin.")
    # print_fish_board(fish_board, scent_board)
    # print(fishes)

print(sum_of_fishes())