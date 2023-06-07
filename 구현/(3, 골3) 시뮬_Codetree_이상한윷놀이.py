# 16:40~
# (1, 골3) Codetree_이상한윷놀이

# 말 k개 [번호, 이동 방향]
# 말들을 쌓인다.

# one turn : 1부터 k 순서대로 움직임



# 4개 이상 겹쳐지는 경우 게임 종료

# === input ===
n, k = map(int, input().split())
COLOR_GRID = [list(map(int, input().split())) for _ in range(n)]
horse_list = [[[0, 0], 0, 0]]
LOC, DIRECTION, PARENT = 0, 1, 2


# === algorithm ===
# n*n grid
WHITE, RED, BLUE = 0, 1, 2
horse_grid = [[list() for _ in range(n)] for _ in range(n)]


def init_horse_grid():
    global horse_list

    def map_direction(d):
        if d == 1:
            return 3
        elif d == 2:
            return 1
        elif d == 3:
            return 0
        elif d == 4:
            return 2

    for _ in range(k):
        new_horse = list(map(int, input().split()))
        new_horse = [[new_horse[0] - 1, new_horse[1] - 1], map_direction(new_horse[2])]
        horse_list.append(new_horse)

    for horse_id in range(1, k + 1):
        r, c = horse_list[horse_id][LOC]
        horse_grid[r][c] += [horse_id]

    print_debug()


def move_all_horse():
    # 이동하려는 칸
    direction_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def move_one_horse():
        global horse_grid, horse_list

        def move_with_above(next_loc, red=False):
            nr, nc = next_loc

            # 이동 말 인덱스
            horse_index = horse_grid[r][c].index(horse_id)

            # 상위 말과 이동
            if red:
                horse_grid[nr][nc] += list(reversed(horse_grid[r][c][horse_index:]))
            else:
                horse_grid[nr][nc] += horse_grid[r][c][horse_index:]
            horse_grid[r][c] = horse_grid[r][c][:horse_index]
            for hid in horse_grid[nr][nc]:
                horse_list[hid][LOC] = [nr, nc]

        def move_to_blue():
            # BLUE -> 방향 바꾸고 이동
            # 이동하는 말만 방향 바꿈
            horse_list[horse_id][DIRECTION] = (d + 2) % 4
            dr, dc = direction_list[(d + 2) % 4]
            nr, nc = r + dr, c + dc

            # 반대 칸이 파란 색이면 이동 X
            if not(0 <= nr < n and 0 <= nc < n) or COLOR_GRID[nr][nc] == BLUE:
                pass
            elif COLOR_GRID[nr][nc] == RED:
                move_with_above([nr, nc], red=True)
            elif COLOR_GRID[nr][nc] == WHITE:
                move_with_above([nr, nc])

        def move_to_white():
            # WHITE -> 이동
            move_with_above([nr, nc])

        def move_to_red():
            # RED -> 칸 뒤집고 이동
            move_with_above([nr, nc], red=True)

        [r, c], d = horse_list[horse_id]
        dr, dc = direction_list[d]
        [nr, nc] = [r + dr, c + dc]

        # 경계 -> BLUE
        if not (0 <= nr < n and 0 <= nc < n):
            move_to_blue()
        elif COLOR_GRID[nr][nc] == WHITE:
            move_to_white()
        elif COLOR_GRID[nr][nc] == RED:
            move_to_red()
        elif COLOR_GRID[nr][nc] == BLUE:
            move_to_blue()

    for horse_id in range(1, k + 1):
        prev_loc = horse_list[horse_id][LOC]
        move_one_horse()
        now_loc = horse_list[horse_id][LOC]
        print_debug(f"move {horse_id}, {prev_loc} -> {horse_list[horse_id][LOC]}")
        if len(horse_grid[now_loc[0]][now_loc[1]]) == 4:
            return True
    return False


def check_grid():

    for hid in range(1, k + 1):
        r, c = horse_list[hid][LOC]
        if len(horse_grid[r][c]) >= 4:
            return True
    return False


def print_debug(title=""):
    if not debug:
        return

    print("============")
    print(title)
    print(horse_list[1:])
    for r in range(n):
        print(*horse_grid[r], "\t\t\t", *COLOR_GRID[r])
    print("============")


# === output ===
# ans: 종료되는 턴의 번호, 1000보다 크거나 불가능 -> -1
debug = False

init_horse_grid()


ans = -1
for turn in range(1, 1001):
    if move_all_horse():
        ans = turn
        break
print(ans)



