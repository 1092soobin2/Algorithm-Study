# (2) (256) 구현__BOJ_19237_어른상어

# M마리 상어
# - 1 > 2 > 3 ...

import copy

# ===input===
N, M, k = map(int, input().split())
input_board = [list(map(int, input().split())) for _ in range(N)]


# 1:up, 2:down, 3: left, 4: right
# direction_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
direction_list = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
# def map_direction(direction: int) -> int:
#     if direction == 1:
#         return 0
#     elif direction == 2:
#         return 2
#     elif direction == 3:
#         return 1
#     elif direction == 4:
#         return 3


shark_directions = list(map(int, input().split()))

priority_list = list()
for _ in range(M):
    tmp_list = [[]]
    for _ in range(4):
        # up, down, left, right
        tmp_list.append(list(map(int, input().split())))
    # tmp_list2 = [tmp_list[0], tmp_list[2], tmp_list[1], tmp_list[3]]
    priority_list.append(tmp_list)

# ===algorithm===
# [id, (r, c), d]
sharks = [[] for _ in range(M + 1)]
# [id, scent]
scent_board = [[[0, 0] for _ in range(N)] for _ in range(N)]

num_of_shark = M

def pre_process(s_board, s_dlist):
    for r in range(N):
        for c in range(N):
            if s_board[r][c] != 0:
                shark_id = s_board[r][c]
                sharks[shark_id] = [shark_id, (r, c), s_dlist[shark_id-1]]
                scent_board[r][c] = [shark_id, k]


# 1. Move shark
# 재귀가 아니므로 copy 인자로 전달 필요 x
def move_sharks(shark_list):
    def check_boundary(index_row, index_col):
        return 0 <= index_row < N and 0 <= index_col < N
    def check_smell(index_row, index_col):
        return scent_board[index_row][index_col][1] != 0
    def whose_smell(index_row, index_col):
        return scent_board[index_row][index_col][0]


    def move_shark_from_to(shark_info) -> (int, int):
        s_id, (r, c), curr_d = shark_info
        # 1) 아무 냄새가 없는 칸
        for next_d in priority_list[s_id-1][curr_d]:
            dr, dc = direction_list[next_d]
            nr, nc = r + dr, c + dc
            # if check_boundary(nr, nc) and scent_board[nr][nc][1] == 0:
            if check_boundary(nr, nc) and not check_smell(nr, nc):
                return (nr, nc), next_d
        # 2) 자신의 냄새가 있는 칸
        for next_d in priority_list[s_id-1][curr_d]:
            dr, dc = direction_list[next_d]
            nr, nc = r + dr, c + dc
            # if check_boundary(nr, nc) and scent_board[nr][nc][0] == s_id:
            if check_boundary(nr, nc) and whose_smell(nr, nc) == s_id:
                    return (nr, nc), next_d
    for shark in shark_list:
        if shark:
            shark[1], shark[2] = move_shark_from_to(shark)


# 2. Update scent_board
def update_scent_board(moved_shark_list):

    # 1) 1초가 흐름 (모든 칸에서 -1)
    for r in range(N):
        for c in range(N):
            if scent_board[r][c][1] > 0:
                scent_board[r][c][1] -= 1
                if scent_board[r][c][1] == 0:
                    scent_board[r][c][0] = 0


    # 2) 움직인 상어들 냄새 업데이트
    for shark in moved_shark_list:
        if shark:
            s_id, (r, c), _ = shark
            global num_of_shark
            if scent_board[r][c][1] == k and s_id > scent_board[r][c][0]:
                # moved_shark_list.remove(shark)
                moved_shark_list[s_id] = []
                num_of_shark -= 1
            elif scent_board[r][c][1] == k and s_id < scent_board[r][c][0]:
                # moved_shark_list.remove(list(filter(lambda x: x[0] == scent_board[r][c][0], moved_shark_list))[0])
                moved_shark_list[scent_board[r][c][0]] = []
                num_of_shark -= 1
                scent_board[r][c][0] = s_id
                scent_board[r][c][1] = k
            else:
                scent_board[r][c][0] = s_id
                scent_board[r][c][1] = k


# ===output===
def print_board(arr):
    print("__________", ans)
    for r in range(N):
        for c in range(N):
            print(arr[r][c], end=' ')
        print()
    print("__________")
    print()

pre_process(input_board, shark_directions)
ans = 0
while ans <= 1000 and num_of_shark != 1:
    move_sharks(sharks)
    update_scent_board(sharks)
    # print(f"sharks: {sharks}")
    # print_board(scent_board)
    ans += 1
# TODO: 1000초 넘으면 -1
# print(ans)
print(ans if ans <= 1000 else -1)
