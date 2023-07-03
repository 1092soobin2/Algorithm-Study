# (0.5, 골5) 시뮬_Codetree_나무타이쿤


# n*n grid (지구)
# 리브로수 [높이, 위치]
# 영양제 : 1증가

# 이동 규칙 [direction, speed]

# === input ===
N, M = map(int, input().split())
tree_grid = [list(map(lambda x: [int(x), False], input().split())) for _ in range(N)]       # [height(높이), 마크]
move_info_list = [list(map(int, input().split())) for _ in range(M)]
essence_list = [[N - 2, 0], [N - 2, 1],
                [N - 1, 0], [N - 1, 1]]
HEIGHT, MARK = 0, 1


# === algorithm ===

# 1. move_essence : 특수 영양제를 이동 규칙에 따라 이동시킴
# move_info : [이동 방향, 속도] 리스트
def move_essence(move_info: list):
    global essence_list
    direction_list = [[0, 0],
                      [0, 1], [-1, 1], [-1, 0], [-1, -1],
                      [0, -1], [1, -1], [1, 0], [1, 1]]
    [dr, dc], speed = direction_list[move_info[0]], move_info[1]

    def move(x):
        x[0] = (x[0] + dr * speed) % N
        x[1] = (x[1] + dc * speed) % N
        return x

    essence_list = list(map(move, essence_list))

    print_debug()


# 2. inject_essence : 특수 영양제 이동 후 칸에 투입됨
def inject_essence():
    global tree_grid
    for r, c in essence_list:
        tree_grid[r][c][HEIGHT] += 1
        tree_grid[r][c][MARK] = True

    print_debug()


# 3. grow_tree
def grow_tree():
    global tree_grid

    grow_list = []
    #   - 특수 영양제 투입 칸의 대각선 칸에
    for r, c in essence_list:
        #   - tree 개수만큼 성장함
        grew = 0
        for dr, dc in [[-1, -1], [1, -1], [1, 1], [-1, 1]]:
            nr, nc = r + dr, c + dc
            #   ! 격자 넘으면 안 센다
            if 0 <= nr < N and 0 <= nc < N and tree_grid[nr][nc][HEIGHT] != 0:
                grew += 1
        grow_list.append(grew)

    for i, [r, c] in enumerate(essence_list):
        tree_grid[r][c][HEIGHT] += grow_list[i]

    print_debug()


# 4. cut_tree
def cut_tree():
    global tree_grid, essence_list

    new_essence_list = []

    for r in range(N):
        for c in range(N):
            #   - 2번에서 자란 tree 제외하고,
            if tree_grid[r][c][MARK]:
                tree_grid[r][c][MARK] = False       # 1년이 지나면 초기화
                continue

            #   - 높이가 2 이상인 tree
            if tree_grid[r][c][HEIGHT] >= 2:
                #   - 높이 -= 2 , essence += 1
                tree_grid[r][c][HEIGHT] -= 2
                new_essence_list.append([r, c])

    essence_list = new_essence_list

    print_debug()


# 1년
def one_year(itr):
    move_essence(move_info_list[itr])
    inject_essence()
    grow_tree()
    cut_tree()


# M년
# return : tree 높이의 총합
def solution() -> int:
    for m in range(M):
        one_year(m)

    sum_of_height = 0
    for r in range(N):
        for c in range(N):
            sum_of_height += tree_grid[r][c][HEIGHT]

    return sum_of_height


def print_debug(title=""):
    if not DEBUG:
        return
    print("==============================")
    print(title)
    print(f"essence: {essence_list}")
    for r in range(N):
        for c in range(N):
            print(f"{tree_grid[r][c][HEIGHT]:4}", end="")
        print()
    print("==============================")


# === output ===
DEBUG = False
# DEBUG = True
print(solution())
