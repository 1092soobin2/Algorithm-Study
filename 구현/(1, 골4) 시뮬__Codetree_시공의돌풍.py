# (1, 골4) 시뮬__Codetree_시공의돌풍

# n*m gird

# tornado: [x][0]에 존재, 크기 2


# === input ===
N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
TORNADO, TORNADO_LOC = -1, []
DIRECTION_LIST_CLOCK = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# === algorithm ===
def init_tornado_loc():
    for r in range(N):
        if grid[r][0] == TORNADO:
            TORNADO_LOC.append([r, 0])

    if debug:
        print_debug(f"[init 이후]: {TORNADO_LOC}")

# 1. 먼지의 확산: 인접 4칸
def diffuse_dust():
    global grid
    new_grid = [[0]*M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            # 돌풍이 있는 자리면 continue
            if grid[r][c] == TORNADO:
                new_grid[r][c] = TORNADO
                continue

            diffused = 0
            for dr, dc in DIRECTION_LIST_CLOCK:
                nr, nc = r + dr, c + dc
                # 1) tornado || not gird -> X
                # 2) [nr][nc] += [r][c] // 5
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != TORNADO:
                    new_grid[nr][nc] += grid[r][c] // 5
                    diffused += grid[r][c] // 5
            # 3) [r][c] -= ([r][c] // 5) * (num of 확산된 칸)
            new_grid[r][c] += (grid[r][c] - diffused)

    # 4) 일괄 진행
    grid = new_grid

    if debug:
        print_debug("[먼지 확산 이후]")


# 2. tornado의 청소
def clean_tornado():
    global grid

    def wind(start_loc, change):
        # 2) 바람 방향대로 한 칸씩 이동
        # 3) 먼지가 없는 바람, 시공의 돌풍으로 들어간 먼지는 사라진다.
        direction_id = 1

        # 처음 칸
        dr, dc = DIRECTION_LIST_CLOCK[1]
        r, c = start_loc[0] + dr, start_loc[1] + dc
        nr, nc = r + dr, c + dc

        curr_dust = grid[r][c]    # 다음 먼지 저장
        grid[r][c] = 0

        while [nr, nc] != start_loc:

            # 다음 칸으로 이동
            r, c = nr, nc
            nr, nc = r + dr, c + dc
            # 벽에 부딪히면 방향 변경
            if not (0 <= nr < N and 0 <= nc < M):
                direction_id = (direction_id + change) % 4
                dr, dc = DIRECTION_LIST_CLOCK[direction_id]
                nr, nc = r + dr, c + dc

            # 먼지 이동
            grid[r][c], curr_dust = curr_dust, grid[r][c]

    # 1) 위칸-반시계, 아래칸-시계
    wind(TORNADO_LOC[0], -1)
    wind(TORNADO_LOC[1], 1)

    if debug:
        print_debug("[바람 분 후]")




def one_second():
    diffuse_dust()
    clean_tornado()


def print_debug(title=""):
    print("=================")
    print(title)
    for r in range(N):
        for c in range(M):
            print(f"{grid[r][c]:3}", end="")
        print()
    print("=================")


# === output ===
# ans: t초 후 먼지의 양
debug = False

init_tornado_loc()
for _ in range(T):
    one_second()
print(sum(map(sum, grid)) + 2)
