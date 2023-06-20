# (3, 플5) Codetree_냉방시스템

# n*n grid


# === input ===
N, M, K = map(int, input().split())     # grid, num of wall, cool
PLACE = [list(map(int, input().split())) for _ in range(N)]
# (x, y, 0) -> 위에 벽이 있다. (x, y, 1) -> 온쪽에 벾이 있다.
WALL_LIST = [list(map(int, input().split())) for _ in range(M)]


# === algorithm ===
# EMTPY, OFFICE = 0, 1
# LEFT, UP, RIGHT, DOWN = 2, 3, 4, 5
WALL = []       # 위, 왼쪽
AIRCONDITIONER_LIST = []
OFFICE_LIST = []
grid = [[0]*N for _ in range(N)]


def init():
    global WALL, AIRCONDITIONER_LIST, OFFICE_LIST

    for r in range(N):
        for c in range(N):
            if PLACE[r][c] == 1:
                OFFICE_LIST.append([r, c])
            elif PLACE[r][c] > 1:
                AIRCONDITIONER_LIST.append([r, c])

    WALL = [[[False, False] for _ in range(N)] for _ in range(N)]
    for wx, wy, s in WALL_LIST:
        WALL[wx-1][wy-1][s] = True

    print_debug(f"init() done. office:{OFFICE_LIST}, air-cond:{AIRCONDITIONER_LIST}")


def check_office():
    # OFFICE 들이 k 이상인지 확인
    for r, c in OFFICE_LIST:
        if grid[r][c] < K:
            return False
    return True


# 1. 에어컨 작동
def cool_air():
    direction_list = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    ddirection_list = [[[-1, -1], [0, -1], [1, -1]],
                       [[-1, -1], [-1, 0], [-1, 1]],
                       [[-1, 1], [0, 1], [1, 1]],
                       [[1, -1], [1, 0], [1, 1]]]

    visited = []

    def init_visited():
        return [[False] * N for _ in range(N)]

    def spread(direction, curr_r, curr_c, acc):
        global grid

        def check_wall():
            if direction == 1 or direction == 3:
                # col 확인 -> row 확인
                if dr != 0 and dc != 0:
                    return WALL[curr_r][max(curr_c, next_c)][1] or WALL[max(curr_r, next_r)][next_c][0]
                else:
                    return WALL[max(curr_r, next_r)][curr_c][0]
            else:
                # row 확인 -> col 확인
                if dr != 0 and dc != 0:
                    return WALL[max(curr_r, next_r)][curr_c][0] or WALL[next_r][max(curr_c, next_c)][1]
                else:
                    return WALL[curr_r][max(curr_c, next_c)][1]

        if acc == 5:
            return

        # 냉방
        grid[curr_r][curr_c] += (5 - acc)
        visited[curr_r][curr_c] = True

        # 3곳으로 전파
        for dr, dc in ddirection_list[direction]:
            next_r, next_c = curr_r + dr, curr_c + dc
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                if check_wall():
                    continue
                spread(direction, next_r, next_c, acc + 1)

    # 벽이 있으면 전파되지 않음
    for r, c in AIRCONDITIONER_LIST:
        visited = init_visited()
        d = PLACE[r][c] - 2
        nr, nc = r + direction_list[d][0], c + direction_list[d][1]
        if 0 <= nr < N and 0 <= nc < N and not WALL[max(r, nr)][max(c, nc)][0 if r != nr else 1]:
            spread(d, nr, nc, 0)
        print_debug(f"cool by {r, c}, {direction_list[PLACE[r][c]-2]}")

    print_debug("cool_air() done." + str(AIRCONDITIONER_LIST))


# 2. 공기 섞임
def mix_air():
    global grid

    # 동시 진행
    new_grid = [grid[r][:] for r in range(N)]

    for r in range(N - 1):
        for c in range(N):
            # 오른쪽 & 아래만 보면 된다.
            for dr, dc in [[0, 1], [1, 0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not WALL[nr][nc][0 if r != nr else 1]:
                    # 높 -> 낮   diff // 4 만큼 전파됨. 1 / 3  3 / 1 -> -
                    new_grid[r][c] += int((grid[nr][nc] - grid[r][c]) / 4)
                    new_grid[nr][nc] -= int((grid[nr][nc] - grid[r][c]) / 4)

    grid = new_grid
    print_debug("mix_air() done.")


# 3. 외벽 칸에 대해서만 시원함 -1
def decrease_cool():
    global grid

    # 0이면 안 감소

    # 위
    for c in range(N-1):
        grid[0][c] = grid[0][c] - 1 if grid[0][c] > 0 else grid[0][c]
    # 오른쪽
    for r in range(N-1):
        grid[r][N - 1] = grid[r][N - 1] - 1 if grid[r][N - 1] > 0 else grid[r][N - 1]
    # 아래
    for c in range(N - 1, 0, -1):
        grid[N - 1][c] = grid[N - 1][c] - 1 if grid[N - 1][c] > 0 else grid[N - 1][c]
    # 왼쪽
    for r in range(N - 1, 0, -1):
        grid[r][0] = grid[r][0] - 1 if grid[r][0] > 0 else grid[r][0]

    print_debug("decrease() done." + str(OFFICE_LIST))


def print_debug(title=""):
    if not DEBUG:
        return
    print("========================================================================")
    print(title)

    for c in range(N):
        print(f"{c:4}", end="")
    print("\t\t\t", end="")
    for c in range(N):
        print(f"{c:^4}", end="")
    print()

    for r in range(N):
        for c in range(N):
            print(f"{grid[r][c]:4}", end="")
        print("\t\t", end="")
        print(r, end="\t")
        for c in range(N):
            print_char = ""
            if WALL[r][c][1]:
                print_char += "|"
            else:
                print_char += " "
            if WALL[r][c][0]:
                print_char += "---"
            else:
                print_char += " "
            print(f"{print_char:4}", end="")
        print()
    print("========================================================================")


# === output ===
DEBUG = False
DEBUG = True

# ans: 모든 사무실(OFFICE)에서 시원함이 전부 k 이상이 되었을 때
init()
time = 0
while time <= 100 and not check_office():
# while time < 10:
    cool_air()
    mix_air()
    decrease_cool()
    time += 1
print(time if time <= 100 else -1)
