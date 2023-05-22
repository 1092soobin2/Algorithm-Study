# ( 골1) 시뮬__Codetree_팩맨

# 4*4 grid
# m monster [loc, direction]
# 1 man

# === input ===
m, t = map(int, input().split())
packman_loc = list(map(lambda x: int(x) - 1, input().split()))
mon_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]       # 각 칸에 방향별 몬스터 개수 저장
dead_grid = [[0]*4 for _ in range(4)]
for _ in range(m):
    mon_r, mon_c, mon_d = map(lambda x: int(x) - 1, input().split())
    mon_grid[mon_r][mon_c][mon_d] += 1


# === algorithm ===

# 1. duplicate monster
def duplicate_monsters() -> list:
    # 현 위치에서 복제
    # 복제몬은 아직 움직이지 못함
    ret_list = [[list() for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            ret_list[r][c] = mon_grid[r][c][:]

    return ret_list


# 2. move monster
def move_monsters():
    global mon_grid

    direction_list = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

    # 한 칸 단위로 다음 위치와 방향 구하기
    def get_next_loc_and_d(curr_r, curr_c, curr_d):
        # 현 방향으로 한 칸 이동 상하좌우+대각선
        for dd in range(8):
            nd = (curr_d + dd) % 8
            dr, dc = direction_list[nd]
            nr, nc = curr_r + dr, curr_c + dc
            # 시체 O || man O || board X -> 45도 반시계 회전하여 이동
            if 0 <= nr < 4 and 0 <= nc < 4 and [nr, nc] != packman_loc and dead_grid[nr][nc] == 0:
                return nr, nc, nd

        # 8칸 모두 이동 불가면 움직이지 않는다.
        return curr_r, curr_c, curr_d

    new_mon_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
    if debug:
        print(packman_loc)
    for r in range(4):
        for c in range(4):
            for d in range(8):
                if mon_grid[r][c][d] != 0:
                    next_r, next_c, next_d = get_next_loc_and_d(r, c, d)
                    new_mon_grid[next_r][next_c][next_d] += mon_grid[r][c][d]
                    if debug:
                        print(f"{r, c, d} -> {next_r, next_c, next_d}")

    mon_grid = new_mon_grid


# 3. move packman
def move_packman():
    global mon_grid, dead_grid, packman_loc

    path = [[0, 0]] * 3     # 무조건 갱신됨
    max_mon = [-1]

    def dfs(r, c, acc_path, acc_mon):
        # 3칸 이동
        # 몬스터를 가장 많이 먹을 수 있는 방향
        if len(acc_path) == 3:
            if acc_mon > max_mon[0]:
                path[:] = acc_path
                max_mon[0] = acc_mon
            return

        # 상 -> 좌 -> 하 -> 우 우선순위
        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                tmp_mon = mon_grid[nr][nc][:]
                mon_grid[nr][nc] = [0]*8
                dfs(nr, nc, acc_path + [[nr, nc]], acc_mon + sum(tmp_mon))
                mon_grid[nr][nc] = tmp_mon

    dfs(packman_loc[0], packman_loc[1], [], 0)

    # 이동 시에 몬스터 시체를 남김
    # 알은 먹지 않는다.
    for pack_r, pack_c in path:
        if mon_grid[pack_r][pack_c] != [0]*8:
            mon_grid[pack_r][pack_c] = [0]*8
            dead_grid[pack_r][pack_c] = 2
    packman_loc = path[-1]


# 4. destroy_dead
def flow_one_turn():
    global dead_grid

    # 2턴 동안만 유지된다.
    for r in range(4):
        for c in range(4):
            if dead_grid[r][c] > 0:
                dead_grid[r][c] -= 1


# 5. complete_duplicate
def complete_duplicate(dup_grid):
    global mon_grid

    for r in range(4):
        for c in range(4):
            for d in range(8):
                mon_grid[r][c][d] += dup_grid[r][c][d]


def sum_grid():
    total = 0

    for r in range(4):
        for c in range(4):
            for d in range(8):
                total += mon_grid[r][c][d]

    return total


def print_grid(title=""):

    print(title)
    for r in range(4):
        print(*mon_grid[r], end="\t\t")
        print(*dead_grid[r])
    print()


# === output ===
debug = False
for _ in range(t):
    if not debug:
        dup = duplicate_monsters()
        move_monsters()
        flow_one_turn()
        move_packman()
        complete_duplicate(dup)
    else:
        dup = duplicate_monsters()
        print_grid("처음")

        move_monsters()
        print_grid("몬스터 움직임")

        flow_one_turn()

        move_packman()
        print_grid("팩맥 움직임")

        complete_duplicate(dup)
        print_grid("다 움직임")


print(sum_grid())
