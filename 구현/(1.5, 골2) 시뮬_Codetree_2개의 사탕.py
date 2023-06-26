# (1, 골2) Codetree_2개의 사탕 19:27~

# N * M board

# red1, blue2





# === input ===
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
HOLE_LOC = [0, 0]
red_loc, blue_loc = [0, 0], [0, 0]
EMPTY, BARRIER, RED, BLUE = '.', '#', 'R', 'B'
INVALID = -1


# === algorithm ===
def init():
    global HOLE_LOC, red_loc, blue_loc
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'O':
                HOLE_LOC = [r, c]
            elif board[r][c] == 'R':
                red_loc = [r, c]
            elif board[r][c] == 'B':
                blue_loc = [r, c]


# 상자 기울이기
# 장애물 || 다른 사탕까지 미끄러짐
def move_balls(curr_red_loc, curr_blue_loc, direction) -> list:
    global board

    ret_red_loc = [0, 0]
    ret_blue_loc = [0, 0]
    dr, dc = direction

    def move_red() -> list:
        red_r, red_c = curr_red_loc
        red_nr, red_nc = red_r + dr, red_c + dc

        # 벽이 아니면 진행
        if curr_red_loc == HOLE_LOC:
            return HOLE_LOC

        while 0 <= red_nr < N and 0 <= red_nc < M and board[red_nr][red_nc] != BARRIER and board[red_nr][red_nc] != BLUE:
            # 다음 위치가 구멍이면 빠지기
            if [red_nr, red_nc] == HOLE_LOC:
                board[curr_red_loc[0]][curr_red_loc[1]] = EMPTY
                return HOLE_LOC
            red_r, red_c = red_nr, red_nc
            red_nr, red_nc = red_r + dr, red_c + dc

        board[curr_red_loc[0]][curr_red_loc[1]] = EMPTY
        board[red_r][red_c] = RED
        return [red_r, red_c]

    def move_blue() -> list:
        blue_r, blue_c = curr_blue_loc
        blue_nr, blue_nc = blue_r + dr, blue_c + dc

        # 벽이 아니면 진행
        while 0 <= blue_nr < N and 0 <= blue_nc < M and board[blue_nr][blue_nc] != BARRIER and board[blue_nr][blue_nc] != RED:
            if [blue_nr, blue_nc] == HOLE_LOC:
                board[curr_blue_loc[0]][curr_blue_loc[1]] = EMPTY
                return HOLE_LOC
            blue_r, blue_c = blue_nr, blue_nc
            blue_nr, blue_nc = blue_r + dr, blue_c + dc

        board[curr_blue_loc[0]][curr_blue_loc[1]] = EMPTY
        board[blue_r][blue_c] = BLUE
        return [blue_r, blue_c]

    curr_red_loc = move_red()
    ret_blue_loc = move_blue()
    ret_red_loc = move_red()

    return ret_red_loc, ret_blue_loc


# red 꺼내기
# blue는 나오면 안 됨. 동시에 나오는 것도 안 됨.
def dfs(curr_red_loc, curr_blue_loc, acc):

    def recover_balls():
        if next_red_loc != HOLE_LOC:
            board[next_red_loc[0]][next_red_loc[1]] = EMPTY
        if next_blue_loc != HOLE_LOC:
            board[next_blue_loc[0]][next_blue_loc[1]] = EMPTY

        board[curr_red_loc[0]][curr_red_loc[1]] = RED
        board[curr_blue_loc[0]][curr_blue_loc[1]] = BLUE

    def get_min_red_cnt(curr_cnt, comp_cnt):
        if curr_cnt != INVALID:
            curr_cnt = min(curr_cnt, comp_cnt)
        else:
            curr_cnt = comp_cnt

        return curr_cnt

    # 10번 이내로 불가능하면 -1 (1부터 시작)
    if acc == 11:
        return -1

    min_red_cnt = INVALID       # ans: red 꺼낼 수 있는 최소 횟수

    for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        # 1. 공 이동시키기
        next_red_loc, next_blue_loc = move_balls(curr_red_loc, curr_blue_loc, direction)

        if curr_red_loc == next_red_loc and curr_blue_loc == next_blue_loc:
            continue

        # 2. 종료 조건 확인
        if next_blue_loc == HOLE_LOC:
            pass
        elif next_red_loc == HOLE_LOC and next_blue_loc != HOLE_LOC:
            # 빨강 색만 빠진 경우 (성공)
            min_red_cnt = get_min_red_cnt(min_red_cnt, acc)
        else:
            # 빨 파 둘 다 안 빠진 경우 (계속)
            result = dfs(next_red_loc, next_blue_loc, acc + 1)
            if result != INVALID:
                min_red_cnt = get_min_red_cnt(min_red_cnt, result)

        print_debug(f"min: {min_red_cnt}, acc: {acc}, direction: {direction}, red: {curr_red_loc} -> {next_red_loc}, blue: {curr_blue_loc} -> {next_blue_loc}")

        # 3. 공 위치 원상복구
        recover_balls()

    return min_red_cnt


def print_debug(title=""):
    if not DEBUG:
        return

    print("===============================")
    print(title)
    for r in range(N):
        for c in range(M):
            print(f"{board[r][c]:2}", end="")
        print()
    print("===============================")


# === output ===
DEBUG = False
DEBUG = True

init()
print(dfs(red_loc, blue_loc, 1))
