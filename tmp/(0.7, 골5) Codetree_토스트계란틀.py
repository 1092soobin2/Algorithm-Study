# (0.7, 골5) Codetree_토스트계란틀


# N*N grid







# === input ===
N, L, R = map(int, input().split())
egg_board = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
wall_board = [[[True, True] for _ in range(N)] for _ in range(N)]       # 아래, 오른쪽


# return: 두 위치 사이의 벽의 유무
def check_wall(curr_loc, next_loc) -> bool:
    [r, c], [nr, nc] = curr_loc, next_loc
    return wall_board[min(r, nr)][min(c, nc)][0 if r != nr else 1]


# 벽의 열림, return: 벽의 열림 여부
def open_wall() -> bool:
    global wall_board

    ret_bool = False            # 벽의 열림 여부

    # L <= 양 <= R
    # 해당 선 분리
    for r in range(N):
        for c in range(N):
            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if L <= abs(egg_board[r][c] - egg_board[nr][nc]) <= R:
                    wall_board[r][c][dc] = False           # dc: 0 -> 아래벽, 1 -> 오른쪽 벽
                    ret_bool = True

    print_debug("open_wall() done.")
    return ret_bool


# 계란 양 변화
def mix_egg():
    global egg_board

    visited = [[False] * N for _ in range(N)]

    def dfs(start):
        sum_of_egg = 0
        egg_list = []           # 추후 섞일 계란들 위치

        # 합쳐진 계란들 찾기, 계란 합 구하기
        stack = [start]
        visited[start[0]][start[1]] = True

        while stack:
            curr_r, curr_c = stack.pop()
            egg_list.append([curr_r, curr_c])
            sum_of_egg += egg_board[curr_r][curr_c]

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and not check_wall([curr_r, curr_c], [nr, nc]):
                    stack.append([nr, nc])
                    visited[nr][nc] = True

        # 계란 섞임
        egg = sum_of_egg // len(egg_list)
        for er, ec in egg_list:
            egg_board[er][ec] = egg

    # 계란 양 변화 (Sum) // (num)
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                dfs([r, c])

    print_debug("mix_egg() done.")


def solution():
    move_cnt = 0
    while True:
        if not open_wall():
            break
        move_cnt += 1
        mix_egg()

    return move_cnt


def print_debug(title=""):
    if not DEBUG:
        return

    print("============================")
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{egg_board[r][c]:3}", end="")
        print("\t\t", end="")
        for c in range(N):
            print(f"{wall_board[r][c]:}", end="")
        print()
    print("============================")


# === output ===
DEBUG = False
DEBUG = True
print(solution())
