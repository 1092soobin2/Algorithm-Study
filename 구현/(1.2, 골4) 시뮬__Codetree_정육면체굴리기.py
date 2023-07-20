# (1, 골4) __Codetree_정육면체굴리기 22:15~

# N*M grid [0-9]
# cube [0]

# ans: 이동 시마다 cube의 상단 숫자

# === input ===
N, M, X, Y, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
roll_list = list(map(int, input().split()))

cube = [0] * 6      # 남쪽 방향(3) 면 번호: 0->1->2->3, 동쪽 방향(1) 면 번호: 0->4->2->5
cube_info = [0, 1, 2]   # 면 번호 [위, 앞, 왼]
cube_loc = [X, Y]
DIRECTION_LIST = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]     # 동서 북남


# === algorithm ===
def get_opposite(side_num):
    return (side_num + 3) % 6


# 큐브 굴리기
def roll(direction):
    global cube_loc, cube_info

    dr, dc = DIRECTION_LIST[direction]
    nr, nc = cube_loc[0] + dr, cube_loc[1] + dc

    # 바깥 이동 시도 -> 출력 X
    if not (0 <= nr < N and 0 <= nc < M):
        return False

    # 이동: 아래 면 위치 갱신
    cube_loc = [nr, nc]

    # 윗면 번호 갱신
    if direction == 3:
        cube_info = [cube_info[1], get_opposite(cube_info[0]), cube_info[2]]
    elif direction == 4:
        cube_info = [get_opposite(cube_info[1]), cube_info[0], cube_info[2]]
    elif direction == 1:
        cube_info = [get_opposite(cube_info[2]), cube_info[1], cube_info[0]]
    elif direction == 2:
        cube_info = [cube_info[2], cube_info[1], get_opposite(cube_info[0])]

    return True


# 이동시키기
def move(direction):
    global grid
    # 바닥칸(grid) 수에 따라 grid, cube 숫자가 변함

    # 굴리기 (큐브 위치 변화)
    if not roll(direction):
        return

    r, c = cube_loc
    bottom_num = (cube_info[0] + 3) % 6
    # grid 0 O -> grid 에 cube 수가 복사됨, cube 수는 그대로.
    if grid[r][c] == 0:
        grid[r][c] = cube[bottom_num]
    # grid 0 X -> cube 에 grid 수가 복사됨, grid 수가 0이 됨
    else:
        cube[bottom_num] = grid[r][c]
        grid[r][c] = 0

    print_debug(f"move({direction})")
    print(cube[cube_info[0]])


def print_debug(title=""):
    if not DEBUG:
        return
    print("====================")
    print(title)
    print(f"cube: {cube}, loc: {cube_loc}, cube_info: {cube_info}")
    for r in range(N):
        for c in range(N):
            print(f"{grid[r][c]:4}", end="")
        print()
    print("====================")


# === output ===
DEBUG = False
# DEBUG = True
for rl in roll_list:
    move(rl)
